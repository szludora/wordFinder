import random

from data.direction import Direction

LETTERS: str = "AÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ"

EMPTY: str = "|"

DELTAS: dict = {
    Direction.HORIZONTAL: [(0, 1), (0, -1)],
    Direction.VERTICAL:   [(1, 0), (-1, 0)],
    Direction.DIAGONAL:   [(1, 1), (-1, -1), (1, -1), (-1, 1)],
}


def build_dynamic_data(configuration: dict) -> None:

    words = [w.upper() for w in configuration["requiredWords"]]

    longest = max(len(w) for w in words) # length of the longest word
    cols = max(configuration["minDimensionX"], longest) # set cols so the longest word can fit
    rows = max(configuration["minDimensionY"], longest) # set rows so the longest word can fit

    table = [[EMPTY for _ in range(cols)] for _ in range(rows)]

    for word in words:
        placed = _try_place_word(table, word, rows, cols, max_attempts=200)
        if not placed:
            print(f"Warning: could not place '{word}' after max attempts.")

    # Add random letter to the remaining empty cells
    for r in range(rows):
        for c in range(cols):
            if table[r][c] == EMPTY:
                table[r][c] = random.choice(LETTERS)

    configuration["table"] = table


def _try_place_word(
    table: list[list[str]],
    word: str,
    rows: int,
    cols: int,
    max_attempts: int,
) -> bool:
    for _ in range(max_attempts):
        direction = random.choice(list(Direction))
        dr, dc = random.choice(DELTAS[direction])

        if dr == 0:
            r_lo, r_hi = 0, rows - 1
        elif dr == 1:
            r_lo, r_hi = 0, rows - len(word)
        else:
            r_lo, r_hi = len(word) - 1, rows - 1

        if dc == 0:
            c_lo, c_hi = 0, cols - 1
        elif dc == 1:
            c_lo, c_hi = 0, cols - len(word)
        else:
            c_lo, c_hi = len(word) - 1, cols - 1

        if r_lo > r_hi or c_lo > c_hi:
            continue

        start_r = random.randint(r_lo, r_hi)
        start_c = random.randint(c_lo, c_hi)

        if _can_place(table, word, start_r, start_c, dr, dc):
            _do_place(table, word, start_r, start_c, dr, dc)
            return True

    return False


def _can_place(
    table: list[list[str]],
    word: str,
    start_r: int,
    start_c: int,
    dr: int,
    dc: int,
) -> bool:

    for i, ch in enumerate(word):
        r = start_r + i * dr
        c = start_c + i * dc
        cell = table[r][c]
        if cell != EMPTY and cell != ch:
            return False
    return True


def _do_place(
    table: list[list[str]],
    word: str,
    start_r: int,
    start_c: int,
    dr: int,
    dc: int,
) -> None:

    for i, ch in enumerate(word):
        r = start_r + i * dr
        c = start_c + i * dc
        table[r][c] = ch
