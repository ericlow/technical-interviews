# Q1 — Node.js EventEmitter (Question 1/5)

Implement `createEE({ fn, interval, signal })` that creates an EventEmitter
instance capable of emitting data at a defined interval.

## Parameters

- `opts.fn` — synchronous function; its return value is emitted as the `data` event
- `opts.interval` — milliseconds between `data` events
- `opts.signal` — AbortSignal; when aborted, emit `close` and stop

## Notes

- If `fn` throws, emit the error with the `error` event
- The first `data` event must be emitted **immediately** after the EventEmitter is created

## Example usage

```js
const ac = new AbortController();
let counter = 0;

const e = createEE({
  fn: () => ++counter,
  interval: 300,
  signal: ac.signal,
});

e.on("data", console.log);
e.on("close", () => console.log("closed"));

setTimeout(() => {
  console.log("stopping after 1 second");
  ac.abort();
}, 1000);
// emits data events: 1, 2, 3, 4 then close event
```
