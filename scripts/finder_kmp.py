from data.direction import Direction
from scripts.finder import vertical_search, diagonal_search


def find_words_in_table_kmp(
    table: list[list[str]], words: list[str], directions: list[Direction]
) -> None:
    words_upper = [w.upper() for w in words]

    for direction in directions:
        match direction:
            case Direction.HORIZONTAL:
                horizontal_search(table=table, words=words_upper)
            case Direction.VERTICAL:
                vertical_search(table=table, words=words_upper)
            case Direction.DIAGONAL:
                diagonal_search(table=table, words=words_upper)
            case _:
                raise NotImplementedError(
                    f"Searching in {direction} direction is not implemented."
                )


def build_lps_list(pattern: str) -> list[int]:
    """Build the KMP Longest Prefix Suffix table for a pattern."""
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    return lps


def search_kmp_hybrid(text: str, pattern: str, lps: list[int]) -> list[int]:
    """
    Find all occurrences of pattern in text.

    Uses CPython's C-level str.find() for the actual character matching (fast),
    and KMP's LPS table to calculate smart skip distances after each match.

    For patterns with repeating prefix-suffix (e.g. "ABCABC", lps[-1]=3),
    the skip after a match is (len - lps[-1]) instead of 1, avoiding redundant
    calls to str.find() for positions that can't possibly match.

    For patterns with no prefix-suffix overlap (lps[-1]=0, e.g. "RÉTES"),
    the skip equals the full pattern length — same as naive, but still fast
    because str.find() does the heavy lifting in C.
    """
    results = []
    m = len(pattern)
    if m == 0:
        return results

    skip = m - lps[m - 1]  # KMP-informed skip distance after a match
    start = 0
    text_len = len(text)

    while start <= text_len - m:
        pos = text.find(pattern, start)
        if pos == -1:
            break
        results.append(pos)
        start = pos + max(skip, 1)

    return results


def concate_letters(letters: list[str]) -> str:
    return "".join(letters).upper()


def horizontal_search(table: list[list[str]], words: list[str]) -> None:
    print("Horizontal search result:\n")

    # Precompute LPS tables once per word — KMP preprocessing
    lps_cache = {word: build_lps_list(word) for word in words}

    for i, raw_row in enumerate(table):
        f_row = concate_letters(raw_row)  # forward row
        b_row = f_row[::-1]              # backward row

        for word in words:
            lps = lps_cache[word]

            for pos in search_kmp_hybrid(f_row, word, lps):
                print(f"-> {i+1}. row {pos+1}. col: {word.capitalize()}")

            for pos in search_kmp_hybrid(b_row, word, lps):
                original_col = len(b_row) - pos
                print(f"<- {i+1}. row {original_col}. col: {word.capitalize()}")
    print()

