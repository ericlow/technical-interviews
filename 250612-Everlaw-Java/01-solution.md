# Solution — Tweet Word Stats Counter

## Task 1 & 2 — Local Implementation

```java
TweetWordStatsCounter {
    static Map<String, Long> bigCount = new HashMap<>();

    void onTweet(long tweetId) {
        // Validate tweetId
        if (tweetId <= 0) return;

        String tweet = TwitterApiClient.getContent(tweetId);
        String[] words = tweet.split("[^a-zA-Z0-9']+"); // split on non-word chars

        Map<String, Integer> count = new HashMap<>();
        for (String word : words) {
            String normalized = word.toLowerCase();
            if (normalized.isEmpty()) continue;
            count.merge(normalized, 1, Integer::sum);
        }

        // Merge into global count
        for (Map.Entry<String, Integer> entry : count.entrySet()) {
            bigCount.merge(entry.getKey(), (long) entry.getValue(), Long::sum);
        }
    }

    long getWordCount(String word) {
        return bigCount.getOrDefault(word.toLowerCase(), 0L);
    }
}
```

## Task 3 — Database Selection

**Choice: Redis** for production word counts.

- Word counts are a simple key-value structure: `word → count`
- Redis `INCR` / `INCRBY` are atomic — safe under concurrent writes from many tweet processors
- Sub-millisecond read latency satisfies a real-time lookup API
- Can persist to disk (RDB/AOF) for durability

**Alternative considered: PostgreSQL**
- Works but requires locking or `ON CONFLICT DO UPDATE` for concurrent increments
- Higher latency than Redis for hot-key reads

## Task 4 — Corner Cases for Tokenization

- **Punctuation attached to words**: `"twitter."`, `"Hello!"` → strip trailing/leading punctuation
- **Case sensitivity**: `"Twitter"` and `"twitter"` should count as the same → normalize to lowercase
- **Contractions/apostrophes**: `"don't"` — treat as one word or split? Define policy (keep as-is is simplest)
- **URLs and handles**: `"@user"`, `"https://..."` — likely should be excluded
- **Numbers**: decide whether to count `"123"` as a word
- **Unicode / emoji**: tweets can contain non-ASCII; ensure split regex handles multibyte correctly
- **Empty strings after split**: filter out empty tokens

**Recommended regex**: `[\\s\\p{Punct}]+` with lowercase normalization, filter empties.

## Task 5 — Capacity Planning

```
100M tweets/day
Average tweet: 10 words
→ 1B word tokens/day processed

Unique words (English vocabulary): ~500K-1M
Word count store: 1M keys × ~50 bytes each ≈ 50 MB (fits in Redis RAM easily)

Tweet processing throughput:
100M tweets/day ÷ 86,400 sec ≈ 1,157 tweets/sec peak
Each tweet: fetch content + tokenize + N increments
→ Need multiple consumer workers, queue-backed (e.g. Kafka → workers → Redis INCRBY)

Storage for raw tweets (if stored):
100M × 300 bytes ≈ 30 GB/day
```

**Architecture at scale**: Twitter webhook/stream → Kafka → worker pool → Redis INCRBY
