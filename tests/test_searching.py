from pygments.lexer import words

from data.direction import Direction
from data.parameters import Parameters
from main import main


from enum import Enum


def test_horizontal_forward_backward_case_insensitive(capsys):
    params: Parameters = Parameters()
    params.table = horizontal["table"]
    params.directions = [Direction.HORIZONTAL]
    params.words = [Words_to_find.HAJÓ.name, Words_to_find.LÁNGOS.name, Words_to_find.ÁGYÚ.name,]
    main(params)
    out = capsys.readouterr().out

    assert Words_to_find.HAJÓ.name in out.upper()
    assert Words_to_find.LÁNGOS.name in out.upper()


def test_horizontal_forward_backward_case_insensitive_kmp(capsys):
    params: Parameters = Parameters()
    params.table = horizontal["table"]
    params.directions = [Direction.HORIZONTAL]
    params.words = [Words_to_find.HAJÓ.name, Words_to_find.LÁNGOS.name, Words_to_find.ÁGYÚ.name,]
    params.use_kmp = True
    main(params)
    out = capsys.readouterr().out

    assert Words_to_find.HAJÓ.name in out.upper()
    assert Words_to_find.LÁNGOS.name in out.upper()
    assert Words_to_find.ÁGYÚ.name not in out.upper()


# Note: Dynamic table might insert words in all three directions. Without Vertical search implemented, this one might fail.
def test_horizontal_forward_backward_case_insensitive_dynamic_table(capsys):
    params: Parameters = Parameters()
    params.words = [Words_to_find.HAJÓ.name, Words_to_find.LÁNGOS.name, Words_to_find.ÁGYÚ.name,]
    params.required_words = [Words_to_find.HAJÓ.name, Words_to_find.LÁNGOS.name, ]
    params.dynamic_table_min_x = 20
    params.dynamic_table_min_y = 15
    params.build_dynamic_table = True
    main(params)
    out = capsys.readouterr().out

    assert len(params.table) == 15
    assert Words_to_find.HAJÓ.name in out.upper()
    assert Words_to_find.LÁNGOS.name in out.upper()


# def test_vertical_forward_backward_case_insensitive(capsys):
#     main(table=vertical, directions_to_search=[Direction.VERTICAL])
#     out = capsys.readouterr().out

#     assert Words_to_find.HAJÓ.name in out.upper()
#     assert Words_to_find.LÁNGOS.name in out.upper()


def test_diagonal_forward_backward_case_insensitive(capsys):
    params: Parameters = Parameters()
    params.table = diagonal["table"]
    params.directions = [Direction.DIAGONAL]
    params.words = [Words_to_find.HAJÓ.name, Words_to_find.LÁNGOS.name, Words_to_find.ÁGYÚ.name, ]
    main(params)
    out = capsys.readouterr().out

    assert Words_to_find.HAJÓ.name in out.upper()
    assert Words_to_find.ÁGYÚ.name in out.upper()


class Words_to_find(Enum):
    HAJÓ = "HAJÓ"
    LÁNGOS = "LÁNGOS"
    ÁGYÚ = "ÁGYÚ"


horizontal = {
    "table": [
        ["X", "h", "a", "J", "Ó", "X"],
        ["X", "X", "X", "X", "X", "X"],
        ["S", "o", "g", "N", "á", "l"],
        ["X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
    ],
    "words": ["HAjó", "LánGos"],
}

vertical = {
    "table": [
        ["H", "s", "X", "X", "X", "X"],
        ["a", "o", "X", "X", "X", "X"],
        ["J", "g", "X", "X", "X", "X"],
        ["Ó", "n", "X", "X", "X", "X"],
        ["X", "Á", "X", "X", "X", "X"],
        ["X", "L", "X", "X", "X", "X"],
    ],
    "words": ["haJó", "LÁngoS"],
}

diagonal = {
    "table": [
        ["H", "X", "X", "X", "X", "X"],
        ["X", "a", "ú", "X", "X", "X"],
        ["X", "X", "j", "Y", "X", "X"],
        ["X", "X", "X", "Ó", "G", "X"],
        ["X", "X", "X", "X", "X", "á"],
        ["X", "X", "X", "X", "X", "X"],
    ],
    "words": ["HaJó", "ÁGyú"],
}
