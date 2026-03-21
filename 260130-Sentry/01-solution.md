# Solution — Stack Trace Profiler

## Approach

Build a tree of nodes where each node tracks its name, total count, and ordered children. Walk every trace top-down, incrementing counts. Render with DFS, tracking indentation depth.

## Solution

```python
from collections import OrderedDict

class Node:
    def __init__(self, name: str):
        self.name = name
        self.count = 0
        self.children = OrderedDict()  # name -> Node, preserves insertion order

def count_stack(traces: list[list[str]]) -> str:
    root = Node("__root__")

    for trace in traces:
        node = root
        for func in trace:
            if func not in node.children:
                node.children[func] = Node(func)
            node = node.children[func]
            node.count += 1

    lines = []

    def render(node: Node, depth: int):
        indent = "    " * depth
        lines.append(f"{indent}{node.name}, {node.count * 10} ms")
        for child in node.children.values():
            render(child, depth + 1)

    for child in root.children.values():
        render(child, 0)

    return "\n".join(lines)
```

## Trace through sample input

| trace | functions visited | counts incremented |
|---|---|---|
| ["main", "parse_message"] | main, parse_message | main+1, parse_message+1 |
| ["main", "parse_message"] | main, parse_message | main+1, parse_message+1 |
| ["main", "parse_message", "log"] | main, parse_message, log | main+1, parse_message+1, log(under pm)+1 |
| ["main", "process_message"] | main, process_message | main+1, process_message+1 |
| ["main", "process_message"] | main, process_message | main+1, process_message+1 |
| ["main", "process_message", "write_output", "log"] | main, process_message, write_output, log | each+1 |
| ["main", "parse_message"] | main, parse_message | main+1, parse_message+1 |

Result: main=7 (70ms), parse_message=4 (40ms), log(under parse)=1 (10ms), process_message=3 (30ms), write_output=1 (10ms), log(under write)=1 (10ms)

## Key insight

`log` appears under two different parents (`parse_message` and `write_output`) and is tracked separately because the tree is path-based, not name-based. Two nodes can have the same name at different positions in the tree.
