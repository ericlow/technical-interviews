from collections import OrderedDict

"""
These are the stack trace samples that would yield that data:
"""
[
    ["main", "parse_message"],
    ["main", "parse_message"],
    ["main", "parse_message", "log"],
    ["main", "process_message"],
    ["main", "process_message"],
    ["main", "process_message", "write_output", "log"],
    ["main", "parse_message"],
]

"""
main, 70 ms
    parse_message, 40 ms
        log, 10ms <---
    process_message, 30 ms
        write_output, 10 ms
            log, 10ms
"""


class Method:
    def __init__(self):
        self.indentation = 0
        self.name = ""
        self.count = ""
        self.methods = OrderedDict()


def count_stack(traces: list[str]) -> str:
    m = Method()
    for record in traces:
        path = ""
        indent = 0
        m.name = record[0]
        m.count += 10

        for index in range(1, len(record) - 1):
            func = record[index]
            if not func in m.methods:
                m.methods[func] = Method()
                m.methods[func].name = func
                m.methods[func].count = 0
                indent += 1
                m.methods[func].indent = indent
            nm = m.methods[func]
            nm.count += 10