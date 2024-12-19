import pytest
from calc import tokenize_expression

def test_tokenize_expression_simple():
    assert tokenize_expression("+ 1 * 8 5") == ["+","1","*","8","5"]
    # Invalid syntax should also be tokenize_expressiond
    assert tokenize_expression("+ 1 / / 5") == ["+","1","*","8","5"]
    assert tokenize_expression("1 2 3 4") == ["1", "2", "3", "4"]

def test_tokenize_multiple_spaces():
    assert tokenize_expression("+  1 *   8 5") == ["+","1","*","8","5"]
    # Invalid syntax should also be tokenize_expressiond
    assert tokenize_expression("   +  1 /     / 5") == ["+","1","*","8","5"]
    assert tokenize_expression("1    2   3     4   ") == ["1", "2", "3", "4"]
    assert tokenize_expression("    1    2   3     4   ") == ["1", "2", "3", "4"]

def test_tokenize_empty_string():
    assert tokenize_expression("") == []
