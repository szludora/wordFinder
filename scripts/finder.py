from data.direction import Direction


def find_words_in_table(
    table: list[list[str]], words: list[str], directions: list[Direction], isKMP: bool
) -> None:
    words_upper = [w.upper() for w in words]

    for direction in directions:
        match direction:
            case Direction.HORIZONTAL:
                horizontal_search(table=table, words=words_upper, isKMP=isKMP)
            case Direction.VERTICAL:
                vertical_search(table=table, words=words_upper)
            case Direction.DIAGONAL:
                diagonal_search(table=table, words=words_upper)
            case _:
                raise NotImplementedError(
                    f"Searching in {direction} direction is not implemented."
                )


def concate_letters(letters: list[str]) -> str:
    return "".join(letters).upper()


def horizontal_search(table: list[list[str]], words: list[str], isKMP: bool) -> None:
    print("Horizontal search result:\n")
    if isKMP:
        lps_cache = {word: build_lps_list(word) for word in words}
        for i, raw_row in enumerate(table):
            f_row = concate_letters(raw_row)  # forward row
            b_row = f_row[::-1]  # backward row

            for word in words:
                lps = lps_cache[word]

                for pos in search_kmp(f_row, word, lps):
                    print(f"-> {i + 1}. row {pos + 1}. col: {word.capitalize()}")

                for pos in search_kmp(b_row, word, lps):
                    original_col = len(b_row) - pos
                    print(f"<- {i + 1}. row {original_col}. col: {word.capitalize()}")
        print()
    else:
        for i, raw_row in enumerate(table):
            f_row = concate_letters(raw_row)  # forward row
            b_row = f_row[::-1]  # backward row

            for word in words:
                if word in f_row:
                    print(f"-> {i + 1}. row {f_row.find(word) + 1}. col: {word.capitalize()}")
                if word in b_row:
                    print(f"<- {i + 1}. row {len(b_row) - b_row.find(word) - 1}. col: {word.capitalize()}")
        print()


def vertical_search(table: list[list[str]], words: list[str]) -> None:
    pass

def diagonal_search(table: list[list[str]], words: list[str]) -> None:
    print("Diagonal search result:\n")

    rows = len(table)
    cols = len(table[0])

    for word in words:
        length = len(word)

        # forward diagonal ↘
        for i in range(rows):
            for j in range(cols):
                if i + length <= rows and j + length <= cols:
                    letters = [table[i+k][j+k] for k in range(length)]
                    if "".join(letters).upper() == word:
                        print(f"↘ {i+1}. row {j+1}. col: {word.capitalize()}")

        # backward diagonal ↖
        for i in range(rows):
            for j in range(cols):
                if i - length >= -1 and j - length >= -1:
                    letters = [table[i-k][j-k] for k in range(length)]
                    if "".join(letters).upper() == word:
                        print(f"↖ {i+1}. row {j+1}. col: {word.capitalize()}")

        # forward diagonal ↙
        for i in range(rows):
            for j in range(cols):
                if i + length <= rows and j - length >= -1:
                    letters = [table[i+k][j-k] for k in range(length)]
                    if "".join(letters).upper() == word:
                        print(f"↙ {i+1}. row {j+1}. col: {word.capitalize()}")

        # backward diagonal ↗
        for i in range(rows):
            for j in range(cols):
                if i - length >= -1 and j + length <= cols:
                    letters = [table[i-k][j+k] for k in range(length)]
                    if "".join(letters).upper() == word:
                        print(f"↗ {i+1}. row {j+1}. col: {word.capitalize()}")

    print()

def build_lps_list(pattern: str) -> list[int]:
    """
        LPS: Longest Prefix Sufix
        The longest first X character repeated for a second time in the given pattern.
        A list of int is built:
        'ABCaabDdabc' -> [0,0,0,1,1,0,0,0,1,2,3]
        From this we know whenever a given pattern fails at index X what shift we should use to move the current search index.
    """
    pattern_len = len(pattern)
    lps = [0] * pattern_len
    length = 0
    i = 1

    while i < pattern_len:
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


def search_kmp(text: str, pattern: str, lps: list[int]) -> list[int]:
    """
        Knuth–Morris–Pratt algorithm
        This algorythm search for the longest repeated prefix. Then, once a sequence proved to be wrong or a full match,
        does not jump back to the original index to continue execution, but rather shift the index considering the lps.
        If the values in the LPS are zeros, this approach is slightly slower than a naive algorythm (this is our case).
        If the values are usually greater than 0, this could significantly reduce search iteration count.
    """
    results = []
    pattern_len = len(pattern)
    if pattern_len == 0:
        return results

    skip = pattern_len - lps[pattern_len - 1]  # KMP-informed skip distance after a match
    start = 0
    text_len = len(text)

    while start <= text_len - pattern_len:
        pos = text.find(pattern, start)
        if pos == -1:
            break
        results.append(pos)
        start = pos + max(skip, 1)

    return results