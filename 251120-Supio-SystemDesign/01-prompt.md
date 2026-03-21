# Supio — System Design: Legal Document Deadline Extraction (LLM Pipeline)

## Type
System design — take-home written document + discussion

## Background

In litigation, courts impose strict deadlines that are not always explicit:
- "Defendant must respond within 30 days"
- "Discovery must be completed by June 15, 2025"
- Scheduling orders with multiple hearing and filing deadlines

Paralegals/docket clerks manually read documents and enter dates into specialized software — slow and error-prone. This is called **docket control** or **critical date management**.

## Problem

Design a system to automate extraction of key dates/deadlines from litigation documents.

**In scope**: extract deadlines from uploaded documents, notify users for verification
**Out of scope**: managing/tracking confirmed events after verification

## Input Document Types

- PDFs
- Scanned court orders (JPG, PNG)
- Formatted text (emails as text files)
- Word documents

## Functional Requirements

- Accept multiple media types (PDF, image, text)
- Extract key deadlines, events, obligations from documents
- Notify users when extraction is ready for review (human-in-the-loop)

## Non-Functional Requirements

- Accuracy ≥ 99%
- High consistency for stored events (inconsistency = material legal damages)
- Record retrieval latency < 0.2 sec
- Scale to 1,000 documents/day with processing latency ≤ 15 min

## Core Entities

- **Client** — law firm using the system
- **User** — lawyer or paralegal who verifies extracted data
- **Case** — litigation case being tracked
- **Document** — uploaded artifact expected to contain events
- **ExtractedCalendarEntry** — unverified calendar event extracted by LLM
- **CalendarEntry** — verified calendar event
- **Event** — real event with date and time (a CalendarEntry may repeat)
