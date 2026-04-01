from data.direction import Direction
from colorama import Fore, Style, init
init()

def find_words_in_table(
    table: list[list[str]], words: list[str], directions: list[Direction]
) -> None:
    words_upper = [w.upper() for w in words]
    all_forward = set()
    all_backward = set()

    for direction in directions:
        match direction:
            case Direction.HORIZONTAL:
                fwd, bwd = horizontal_search(table=table, words=words_upper)
                all_forward.update(fwd)
                all_backward.update(bwd)
            case Direction.VERTICAL:
                fwd, bwd = vertical_search(table=table, words=words_upper)
                all_forward.update(fwd)
                all_backward.update(bwd)
            case Direction.DIAGONAL:
                fwd, bwd = diagonal_search(table=table, words=words_upper)
                all_forward.update(fwd)
                all_backward.update(bwd)
            case _:
                raise NotImplementedError(
                    f"Searching in {direction} direction is not implemented."
                )

    return all_forward, all_backward

def concate_letters(letters: list[str]) -> str:
    return "".join(letters).upper()


def horizontal_search(table: list[list[str]], words: list[str]) -> tuple[set, set]:
    print("Horizontal search result:\n")
    forward_positions = set()
    backward_positions = set()
    
    for i, raw_row in enumerate(table):
        f_row = concate_letters(raw_row)  # forward row
        b_row = f_row[::-1]  # backward row

        for word in words:
            if word in f_row:
                start = f_row.find(word)
                for k in range(len(word)):
                    forward_positions.add((i, start + k))
                print(Fore.GREEN + f"-> {i+1}. row {start+1}. col: {word.capitalize()}" + Style.RESET_ALL)
            if word in b_row:
                start = b_row.find(word)
                for k in range(len(word)):
                    backward_positions.add((i, len(b_row) - start - k - 1))
                print(Fore.YELLOW + f"<- {i+1}. row {len(b_row) - start}. col: {word.capitalize()}" + Style.RESET_ALL)
    print()
    return forward_positions, backward_positions


def vertical_search(table: list[list[str]], words: list[str]) -> tuple[set, set]:
    return set(), set()

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
    return set(), set()