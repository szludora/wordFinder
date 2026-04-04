from pygments.lexer import words

from data.direction import Direction
from data.parameters import Parameters
from main import main


from enum import Enum

from scripts.build_dynamic_data import build_dynamic_data


def test_horizontal_forward_backward_case_insensitive(capsys):
    params: Parameters = Parameters()
    params.table = horizontal["table"]
    params.directions = [Direction.HORIZONTAL]
    params.words = [Words_to_find.HAJÓ.name, Words_to_find.LÁNGOS.name, Words_to_find.ÁGYÚ.name,]
    main(params)
    out = capsys.readouterr().out

    assert Words_to_find.HAJÓ.name in out.upper()
    assert Words_to_find.LÁNGOS.name in out.upper()

"""
    KMP Algorythm related tests
        • Simple test
        • Case sensibility test
        • Palindrome test
        • Negative test
"""
def test_horizontal_forward_backward_kmp_simple(capsys):
    params: Parameters = Parameters()
    params.table = horizontal["table"]
    params.directions = [Direction.HORIZONTAL]
    params.words = [Words_to_find.HAJÓ.name, Words_to_find.LÁNGOS.name, Words_to_find.ÁGYÚ.name,]
    params.use_kmp = True
    main(params)
    out = capsys.readouterr().out

    assert Words_to_find.LÁNGOS.name in out.upper()
    assert Words_to_find.HAJÓ.name in out.upper()


def test_horizontal_forward_backward_kmp_case_insensitive(capsys):
    params: Parameters = Parameters()
    params.table = horizontal["table"]
    params.directions = [Direction.HORIZONTAL]
    params.words = horizontal["words"]
    params.use_kmp = True
    main(params)
    out = capsys.readouterr().out

    assert Words_to_find.HAJÓ.name in out.upper()
    assert Words_to_find.LÁNGOS.name in out.upper()


def test_horizontal_forward_backward_kmp_palindrome(capsys):
    params: Parameters = Parameters()
    params.table = horizontal["table"]
    params.directions = [Direction.HORIZONTAL]
    params.words = horizontal["words"]
    params.use_kmp = True
    main(params)
    out = capsys.readouterr().out

    assert out.upper().count(horizontal["words"][2].upper()) == 1

def test_horizontal_forward_backward_kmp_negative(capsys):
    params: Parameters = Parameters()
    params.table = horizontal["table"]
    params.directions = [Direction.HORIZONTAL]
    params.words = [Words_to_find.HAJÓ.name, Words_to_find.LÁNGOS.name, Words_to_find.ÁGYÚ.name,]
    params.use_kmp = True
    main(params)
    out = capsys.readouterr().out

    assert Words_to_find.LÁNGOS.name in out.upper()
    assert Words_to_find.HAJÓ.name in out.upper()
    assert Words_to_find.ÁGYÚ.name not in out.upper()

"""
    Dynamic Table Generation Tests
        • Simple test
        • Table size test
        • Word placement correctness
        • Negative test
"""
def test_dynamic_table_test_simple(capsys):
    params: Parameters = Parameters()
    params.words = [Words_to_find.HAJÓ.name, Words_to_find.LÁNGOS.name,]
    params.required_words = [Words_to_find.HAJÓ.name, Words_to_find.LÁNGOS.name, ]
    params.directions = [Direction.HORIZONTAL]
    params.insert_directions = [Direction.HORIZONTAL]
    params.build_dynamic_table = True
    params.dynamic_table_min_x = 20
    params.dynamic_table_min_y = 15
    build_dynamic_data(params)
    main(params)
    out = capsys.readouterr().out

    assert Words_to_find.HAJÓ.name in out.upper()
    assert Words_to_find.LÁNGOS.name in out.upper()
    assert len(params.table[1]) == 20
    assert len(params.table) == 15

def test_dynamic_table_test_table_size(capsys):
    params: Parameters = Parameters()
    params.insert_directions = [Direction.HORIZONTAL]
    params.required_words = [""]
    params.build_dynamic_table = True
    params.dynamic_table_min_x = 20
    params.dynamic_table_min_y = 15
    build_dynamic_data(params)
    assert len(params.table[1]) == 20
    assert len(params.table) == 15

def test_dynamic_table_test_word_placement_correctness(capsys):
    params: Parameters = Parameters()
    params.table = horizontal["table"]
    params.words = [Words_to_find.HAJÓ.name, Words_to_find.LÁNGOS.name,]
    params.required_words = [Words_to_find.HAJÓ.name, Words_to_find.LÁNGOS.name, ]
    params.insert_directions = [Direction.HORIZONTAL]
    params.build_dynamic_table = True
    params.dynamic_table_min_x = 20
    params.dynamic_table_min_y = 15

    params.directions = [Direction.HORIZONTAL]
    build_dynamic_data(params)
    main(params)
    out = capsys.readouterr().out
    assert Words_to_find.HAJÓ.name in out.upper()
    assert Words_to_find.LÁNGOS.name in out.upper()

    params.insert_directions = [Direction.DIAGONAL]
    build_dynamic_data(params)
    main(params)
    out = capsys.readouterr().out
    assert Words_to_find.HAJÓ.name not in out.upper()
    assert Words_to_find.LÁNGOS.name not in out.upper()

def test_dynamic_table_test_negative(capsys):
    params: Parameters = Parameters()
    params.table = horizontal["table"]
    params.words = [Words_to_find.HAJÓ.name, Words_to_find.LÁNGOS.name,]
    params.required_words = [Words_to_find.HAJÓ.name, Words_to_find.LÁNGOS.name, ]
    params.directions = [Direction.HORIZONTAL]
    params.insert_directions = [Direction.HORIZONTAL]
    params.build_dynamic_table = True
    params.dynamic_table_min_x = 20
    params.dynamic_table_min_y = 15
    build_dynamic_data(params)
    main(params)
    out = capsys.readouterr().out

    assert len(params.table) != len(horizontal["table"])
    assert len(params.table[1]) != len(horizontal["table"][1])
    assert Words_to_find.HAJÓ.name in out.upper()
    assert Words_to_find.LÁNGOS.name in out.upper()

def test_vertical_forward_backward_case_insensitive(capsys):
    params: Parameters = Parameters()
    params.table = vertical["table"]
    params.directions = [Direction.VERTICAL]
    params.words = [Words_to_find.HAJÓ.name, Words_to_find.LÁNGOS.name, Words_to_find.ÁGYÚ.name,]
    main(params)
    out = capsys.readouterr().out

    assert Words_to_find.HAJÓ.name in out.upper()
    assert Words_to_find.LÁNGOS.name in out.upper()


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
        ["X", "A", "b", "b", "A", "X"],
        ["X", "X", "X", "X", "X", "X"],
    ],
    "words": ["HAjó", "LánGos", "AbbA"],
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
