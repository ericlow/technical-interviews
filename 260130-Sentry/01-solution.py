from collections import OrderedDict


class Node:
    def __init__(self, name: str):
        self.name = name
        self.count = 0
        self.children = OrderedDict()  # preserves insertion order


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


if __name__ == "__main__":
    traces = [
        ["main", "parse_message"],
        ["main", "parse_message"],
        ["main", "parse_message", "log"],
        ["main", "process_message"],
        ["main", "process_message"],
        ["main", "process_message", "write_output", "log"],
        ["main", "parse_message"],
    ]

    print(count_stack(traces))
