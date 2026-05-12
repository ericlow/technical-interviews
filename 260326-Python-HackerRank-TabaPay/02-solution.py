from collections import Counter


def spell_check(letters: list[str], words: list[str]) -> list[str]:
    available = Counter(letters)
    return [w for w in words if not (Counter(w) - available)]


def main():
    letters_line = input().split(":", 1)[1]
    letters = [c.strip() for c in letters_line.split(",")]

    words_line = input().split(":", 1)[1]
    words = [w.strip() for w in words_line.split(",")]

    result = spell_check(letters, words)
    print(", ".join(result))


if __name__ == "__main__":
    main()


# --- Driver ---
# Letters: a, b, c, d, e, f
# Words: bad, face, bead, xyz, cafe
# Expected: bad, face, bead, cafe
assert spell_check(list("abcdef"), ["bad", "face", "bead", "xyz", "cafe"]) == [
    "bad", "face", "bead", "cafe"
]

# Letter used more times than available
assert spell_check(["a", "b"], ["aab"]) == []   # needs 2 a's, only 1 available
assert spell_check(["a", "a", "b"], ["aab"]) == ["aab"]

print("All assertions passed.")
