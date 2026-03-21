# Solution — Supio Legal Deadline Extraction System

## Architecture

```
User/Browser → Load Balancer → API Gateway → Digital Media Upload Service
                                                    ↓
                                              Amazon S3 (document storage)
                                           ↙              ↘
                              Lambda (OpenAI path)    Lambda (Anthropic path)
                                  ↓                        ↓
                           OCR (if image)            OCR (if image)
                                  ↓                        ↓
                            OpenAI LLM              Anthropic LLM
                                  ↓                        ↓
                         save ExtractedCalendarEntries → PostgreSQL
                                  ↓                        ↓
                                Amazon SQS (processing complete events)
                                        ↓
                              Result Comparison Service
                                        ↓
                                  Amazon SNS
                               ↙            ↘
                            Email           Slack
```

## Flow

### 1. Upload
- Client uploads document via pre-signed S3 URL
- `Digital Media Upload Service` saves file metadata to PostgreSQL
- Document lands in S3, triggering two Lambda processors in parallel

### 2. Processing (Dual LLM)
- Each Lambda (OpenAI path, Anthropic path) may invoke OCR/image processing for scanned docs
- Extracted text saved as intermediate artifact in PostgreSQL (for auditing/reprocessing)
- Text submitted to LLM for event/deadline extraction
- Results saved as `ExtractedCalendarEntries` (unverified)
- Completion event placed on Amazon SQS

### 3. Result Comparison
- `Result Comparison Service` consumes SQS events
- Waits until both LLMs have completed
- Compares extracted dates between OpenAI and Anthropic results
- **Confidence scoring**: high = both LLMs agree with matching context; low = disagreement or ambiguous language (e.g. "within 30 days of service")
- If high confidence → auto-accept or notify user for light review
- If low confidence → flag for manual review with specialized UI

### 4. User Notification
- SNS publishes to email, Slack, or app
- User reviews and verifies `ExtractedCalendarEntries` → promotes to `CalendarEntry`

## LLM Choice

**OpenAI GPT-4o + Anthropic Claude Sonnet** (dual LLM strategy)
- ML approaches would require fine-tuning for complex relative date expressions
- LLMs handle nuance out of the box with prompt engineering
- Two LLMs reduce systematic single-model error
- Human-in-the-loop remains mandatory regardless of confidence

## Key Design Decisions

- **High consistency**: PostgreSQL for all event storage (CP system — legal accuracy is paramount)
- **Dual LLM with comparison**: reduces systematic errors; confidence score drives human review threshold
- **Intermediate artifact storage**: extracted text saved before LLM call — enables reprocessing without re-OCR
- **Audit trail**: every processing step logged with timestamp and actor

## Error Handling

| Failure | Handling |
|---------|----------|
| OCR failure (poor image quality) | Flag for manual processing, notify user |
| LLM API failure | Retry with exponential backoff, after 3 attempts → DLQ → delayed reprocessing |
| Relative dates ("within 30 days of service") | Extract as-is, low confidence flag, specialized UI for user to resolve |
| Amended orders (modifying previous deadline) | Flag complexity, request user intervention |

## Scalability

- **Primary bottleneck**: LLM API rate limits
- **Mitigation**: SQS queue throttles lambda concurrency; exponential backoff on rate limit errors; DLQ for failed messages → delayed retry schedule

## Capacity Planning

```
1,000 docs/day
Processing budget: 15 min/doc
Peak concurrent processing: ~1,000 / (24h × 4 batches/hr) ≈ manageable with throttled lambdas
Storage: litigation docs are small (PDFs/text) — S3 cost negligible
PostgreSQL: events per doc ~5-20 entries — well within scale
```
