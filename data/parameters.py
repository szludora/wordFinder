import data.datas as tables
from data.direction import Direction


class Parameters:
    use_kmp: bool = False
    build_dynamic_table: bool = False
    table: list[list[str]] = tables.TABLE_2["table"]
    words: list[str] = tables.TABLE_2["words"]
    directions: list[Direction] = [
    Direction.HORIZONTAL,
    Direction.VERTICAL,
    Direction.DIAGONAL,
]
    # Dynamic table build params
    dynamic_table_min_x: int
    dynamic_table_min_y: int
    required_words: list[str]
    insert_directions: list[Direction] = [
    Direction.HORIZONTAL,
    Direction.VERTICAL,
    Direction.DIAGONAL,
]