# Everlaw Interview — Tweet Word Stats Counter (Java)

## Type
Java coding + system design discussion (multi-part)

## Interface

```java
TweetWordStatsCounter {
    void onTweet(long tweetId);
    long getWordCount(String word);
}

TwitterApiClient {
    String getContent(long tweetId);
}
```

## Sample Data

```
Tweet 1 - "setting up my twitter"
Tweet 2 - "I just set up my Twitter. Hello world!"
Tweet 3 - "Hello! My twitter rocks"

getWordCount("twitter") -> 3  // case-insensitive
```

## Tasks

1. **Task 1** — Implement `onTweet` for a local (single-machine) app
2. **Task 2** — Implement `getWordCount`
3. **Task 3** — Select a database for a production `TweetWordStatsCounter` system
4. **Task 4** — Handle corner cases for tokenizing/splitting words
5. **Task 5** — Capacity planning for the system

## Scale (given)

- 100M tweets
- 200 chars / tweet (UTF-8), ~300 bytes per line
- ~10 words per tweet → ~20 bytes per word entry
- 100M tweets × 10 words = 1B word occurrences
- 1B rows × 20 bytes ≈ 20 GB for word index
