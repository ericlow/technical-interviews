def divisible_filter(limit: int, divisor: int) -> list[int]:
    return [n for n in range(1, limit + 1) if n % divisor == 0]


def merge_dicts(d1: dict, d2: dict) -> dict:
    result = {}
    for key in set(d1) | set(d2):
        result[key] = d1.get(key, 0) + d2.get(key, 0)
    return result


def remove_dup_keep_first(lst: list[int]) -> list[int]:
    seen = set()
    result = []
    for n in lst:
        if n not in seen:
            result.append(n)
            seen.add(n)
    return result


def remove_dup_keep_last(lst: list[int]) -> list[int]:
    seen = set()
    result = []
    for n in reversed(lst):
        if n not in seen:
            result.append(n)
            seen.add(n)
    return list(reversed(result))


if __name__ == "__main__":
    print(divisible_filter(20, 3))     # [3, 6, 9, 12, 15, 18]

    d1 = {1: 10, 2: 20}
    d2 = {2: 30, 3: 40, 4: 50}
    print(merge_dicts(d1, d2))         # {1: 10, 2: 50, 3: 40, 4: 50}

    lst = [0, 1, 2, 0, 3, 0]
    print(remove_dup_keep_first(lst))  # [0, 1, 2, 3]
    print(remove_dup_keep_last(lst))   # [1, 2, 3, 0]
