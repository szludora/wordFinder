import sys
import json

import data.datas as tables
from data.direction import Direction
from scripts.finder import find_words_in_table
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
        isKMP=False
    )

    print(f"Elapsed time: {(time.time() - start):.2f} seconds")

    print("##############################  - Alternative ALGORYTHM (KMP) - ##############################")
    directions_to_search = [
        Direction.HORIZONTAL,
    ]
    start = time.time()
    find_words_in_table(
        table=table['table'],
        words=table['words'],
        directions=directions_to_search,
        isKMP=True
    )

    print(f"Elapsed time: {(time.time() - start):.2f} seconds")


def get_config():
    with open("config/config.json","r", encoding="utf-8") as f:
        return json.load(f)

if __name__ == "__main__":
    use_custom_config: bool = "--config:" in sys.argv
    if use_custom_config == False:
        config = get_config()
        if config:
            if config["preDefinedConfig"] and len(config["preDefinedConfig"]) > 0:
                main(table=getattr(tables,config["preDefinedConfig"]))
            build_dynamic_data(config)
            main(config)
        else:
            main()
    else:
        main()
