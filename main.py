import sys

import data.datas as tables
from data.direction import Direction
from scripts.finder import find_words_in_table
from scripts.finder_kmp import find_words_in_table_kmp
from scripts.build_dynamic_data import build_dynamic_data
from scripts.print_table import print_formatted_table
import time

_DIRECTIONS_TO_SEARCH = [
    Direction.HORIZONTAL,
    Direction.VERTICAL,
    Direction.DIAGONAL,
]


def main(table=tables.TABLE_1, directions_to_search=_DIRECTIONS_TO_SEARCH) -> None:

    print_formatted_table(table["table"])
    start = time.time()
    find_words_in_table(
        table=table["table"],
        words=table["words"],
        directions=directions_to_search,
    )

    print(f"Elapsed time: {(time.time() - start):.2f} seconds")

    print("##############################  - Alternative ALGORYTHM (KMP, Horizontal Only) - ##############################")

    start = time.time()
    find_words_in_table_kmp(
        table=table["table"],
        words=table["words"],
        directions=directions_to_search,
    )

    print(f"Elapsed time: {(time.time() - start):.2f} seconds")


if __name__ == "__main__":
    use_custom_table: bool = "--custom" not in sys.argv
    if use_custom_table:
        build_dynamic_data(tables.CONFIGURATION_1)
        main(tables.CONFIGURATION_1)
    else:
        main()
