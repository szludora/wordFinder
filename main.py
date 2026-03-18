import data.datas as tables
from data.direction import Direction
from scripts.finder import find_words_in_table
from scripts.print_table import print_formatted_table


def main() -> None:
    table = tables.TABLE_3

    DIRECTIONS_TO_SEARCH = [
        Direction.HORIZONTAL,
        Direction.VERTICAL,
        Direction.DIAGONAL,
    ]

    print_formatted_table(table["table"])

    find_words_in_table(
        table=table["table"],
        words=table["words"],
        directions=DIRECTIONS_TO_SEARCH,
    )


if __name__ == "__main__":
    main()
