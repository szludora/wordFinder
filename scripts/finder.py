from data.direction import Direction


def find_words_in_table(
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


def concate_letters(letters: list[str]) -> str:
    return "".join(letters).upper()


def horizontal_search(table: list[list[str]], words: list[str]) -> None:
    print("Horizontal search result:\n")
    for i, raw_row in enumerate(table):
        f_row = concate_letters(raw_row)  # forward row
        b_row = f_row[::-1]  # backward row

        for word in words:
            if word in f_row:
                print(f"-> {i+1}. row {f_row.find(word)+1}. col: {word.capitalize()}")
            if word in b_row:
                print(f"<- {i+1}. row {len(b_row) - b_row.find(word)-1}. col: {word.capitalize()}")
    print()


def vertical_search(table: list[list[str]], words: list[str]) -> None:
    print("Vertical search result:\n")

    if not table or not table[0]:
        print()
        return

    row_count = len(table)
    col_count = len(table[0])

    for col in range(col_count):
        top_down = "".join(table[row][col] for row in range(row_count)).upper()
        bottom_up = top_down[::-1]

        for word in words:
            if word in top_down:
                print(f"↓ -> {col+1}. row {top_down.find(word)+1}. col: {word.capitalize()}")

            if word in bottom_up:
                print(f"↑ {len(bottom_up) - bottom_up.find(word)}. row {col+1}. col: {word.capitalize()}")

    print()


def diagonal_search(table: list[list[str]], words: list[str]) -> None:
    pass
