import sys
import io
import data.datas as tables
from data.direction import Direction
from scripts.finder import find_words_in_table
from scripts.print_table import print_formatted_table

_DIRECTIONS_TO_SEARCH = [
    Direction.HORIZONTAL,
    Direction.VERTICAL,
    Direction.DIAGONAL,
]


def main(table=tables.TABLE_1, directions_to_search=_DIRECTIONS_TO_SEARCH) -> None:
    if "pytest" not in sys.modules:
        if isinstance(sys.stdout, io.TextIOWrapper):
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
        if isinstance(sys.stderr, io.TextIOWrapper):
            sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

    print_formatted_table(table["table"])

    find_words_in_table(
        table=table["table"],
        words=table["words"],
        directions=directions_to_search,
    )


if __name__ == "__main__":
    main()
