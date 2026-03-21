var EventEmitter = require("events");

/**
 * @param {object} opts
 * @param {any} opts.fn
 * @param {number} opts.interval
 * @param {AbortSignal} opts.signal
 * @returns {EventEmitter}
 */
const createEE = ({ fn, interval, signal }) => {
  const e = new EventEmitter();

  const emit = () => {
    try {
      e.emit("data", fn());
    } catch (err) {
      e.emit("error", err);
    }
  };

  // Emit immediately, then on each interval
  emit();
  const timer = setInterval(emit, interval);

  signal.addEventListener("abort", () => {
    clearInterval(timer);
    e.emit("close");
  });

  return e;
};
