Spell Check

Input is two parts. First, a comma-separated list of single lowercase letters. Second, a list of lowercase words (one per line or comma-separated).
Given the available letters, return all words from the list that can be fully spelled using only the available letters. Each letter from the set can only be used once per word. Letter availability resets for each word (words are checked independently).

Example input:
Letters: a, b, c, d, e, f
Words: bad, face, bead, xyz, cafe

Example output:
bad, face, bead

xyz fails because those letters aren't available. cafe fails because there is only one a but cafe needs one a, one c, one f, and one e — actually cafe would pass. The word would fail if it needed a letter more times than it appears in the available set.
