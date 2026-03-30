import random

from data.direction import Direction
from data.parameters import Parameters

LETTERS: str = "AÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ"

EMPTY: str = "|"

DELTAS: dict = {
    Direction.HORIZONTAL: [(0, 1), (0, -1)],
    Direction.VERTICAL:   [(1, 0), (-1, 0)],
    Direction.DIAGONAL:   [(1, 1), (-1, -1), (1, -1), (-1, 1)],
}


def build_dynamic_data(params: Parameters) -> None:

    words = [w.upper() for w in params.required_words]

    """Ensure all the required words has a chance to fit into the table."""
    longest = max(len(w) for w in words) # length of the longest word
    cols = max(params.dynamic_table_min_x, longest) # set cols so the longest word can fit
    rows = max(params.dynamic_table_min_y, longest) # set rows so the longest word can fit

    """Define empty start table"""
    table = [[EMPTY for _ in range(cols)] for _ in range(rows)]

    """Try to add every word, indicate in terminal if a word didn't fit."""
    for word in words:
        placed = _try_place_word(table, word, rows, cols, params.insert_directions, max_attempts=200)
        if not placed:
            print(f"Warning: could not place '{word}' after max attempts.")

    """Add random letters to the remaining empty cells."""
    for r in range(rows):
        for c in range(cols):
            if table[r][c] == EMPTY:
                table[r][c] = random.choice(LETTERS)

    params.table = table


def _try_place_word(
    table: list[list[str]],
    word: str,
    rows: int,
    cols: int,
    directions: list,
    max_attempts: int,
) -> bool:
    """Ensure no infinite loop occurs in dense tables."""
    for _ in range(max_attempts):
        direction = random.choice(directions)
        delta_row, delta_col = random.choice(DELTAS[direction])

        """Based on direction, delta and word length, define the min/max indexes we can work with."""
        if delta_row == 0:
            min_start_row_index, max__start_row_index = 0, rows - 1
        elif delta_row == 1:
            min_start_row_index, max__start_row_index = 0, rows - len(word)
        else:
            min_start_row_index, max__start_row_index = len(word) - 1, rows - 1

        if delta_col == 0:
            min_start_col_index, max_start_col_index = 0, cols - 1
        elif delta_col == 1:
            min_start_col_index, max_start_col_index = 0, cols - len(word)
        else:
            min_start_col_index, max_start_col_index = len(word) - 1, cols - 1

        if min_start_row_index > max__start_row_index or min_start_col_index > max_start_col_index:
            continue

        """Pick a random start coordinate within the allowed range."""
        start_r = random.randint(min_start_row_index, max__start_row_index)
        start_c = random.randint(min_start_col_index, max_start_col_index)

        """
            If the word's character sequence does not collide with an other already inserted word's character sequence, 
            then insert the word.
        """
        if _can_place(table, word, start_r, start_c, delta_row, delta_col):
            _do_place(table, word, start_r, start_c, delta_row, delta_col)
            return True

    return False


def _can_place(
    table: list[list[str]],
    word: str,
    start_row: int,
    start_col: int,
    delta_row: int,
    delta_col: int,
) -> bool:

    for i, ch in enumerate(word):
        row = start_row + i * delta_row
        col = start_col + i * delta_col
        cell = table[row][col]
        if cell != EMPTY and cell != ch:
            return False
    return True


def _do_place(
    table: list[list[str]],
    word: str,
    start_row: int,
    start_col: int,
    delta_row: int,
    delta_col: int,
) -> None:

    for i, ch in enumerate(word):
        row = start_row + i * delta_row
        col = start_col + i * delta_col
        table[row][col] = ch
