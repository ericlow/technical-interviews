# Sentry On-Site — Stack Trace Profiler (Python)

## Type
Python coding — data structures, tree traversal

## Problem

Given a list of sampled stack traces, build a profiler that aggregates time per function and displays it as an indented call tree.

Each stack trace represents 10ms of CPU time. Each entry in a trace is a list of function names from outermost (index 0) to innermost (last index).

## Sample Input

```python
traces = [
    ["main", "parse_message"],
    ["main", "parse_message"],
    ["main", "parse_message", "log"],
    ["main", "process_message"],
    ["main", "process_message"],
    ["main", "process_message", "write_output", "log"],
    ["main", "parse_message"],
]
```

## Expected Output

```
main, 70 ms
    parse_message, 40 ms
        log, 10ms
    process_message, 30 ms
        write_output, 10 ms
            log, 10ms
```

## Rules

- Each trace = 10ms
- Time for a function = number of traces it appears in × 10ms
- Children are indented relative to their parent
- Maintain insertion order of children (first time seen)

## Interface

```python
def count_stack(traces: list[list[str]]) -> str:
    ...
```
