from data.direction import Direction
from main import main


from enum import Enum


def test_horizontal_forward_backward_case_insensitive(capsys):
    main(table=horizontal, directions_to_search=[Direction.HORIZONTAL])
    out = capsys.readouterr().out

    assert Words_to_find.HAJÓ.name in out.upper()
    assert Words_to_find.LÁNGOS.name in out.upper()


# def test_vertical_forward_backward_case_insensitive(capsys):
#     main(table=vertical, directions_to_search=[Direction.VERTICAL])
#     out = capsys.readouterr().out

#     assert Words_to_find.HAJÓ.name in out.upper()
#     assert Words_to_find.LÁNGOS.name in out.upper()


def test_diagonal_forward_backward_case_insensitive(capsys):
    main(table=diagonal, directions_to_search=[Direction.DIAGONAL])
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
