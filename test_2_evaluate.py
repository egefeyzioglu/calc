import pytest
from calc import evaluate_tokens

def test_evaluate_simple():
    assert evaluate_tokens(["+","1","10"]) == 11
    assert evaluate_tokens(["*","2","10"]) == 20


def test_evaluate_harder():
    # Let's see if you're doing floating points right
    # If this fails, see https://0.30000000000000004.com/#python-3
    assert evaluate_tokens(["+", "0.1", "0.2"]) == 0.3
    # Something long
    assert evaluate_tokens(["/","6","*","2","+","1","2"]) = 1
    assert evaluate_tokens(["/","6","*","2","-","1","2"]) = -3
    # Operators are allowed to follow each other
    assert evaluate_tokens(["*","/","10","1","10"]) == 100
    assert evaluate_tokens(["*","/","*","/","10","1","10","10","1"]) == 10


def test_operand_order():
    assert evaluate_tokens(["/","10","2"]) == 5
    assert evaluate_tokens(["-","1","10"]) == -9

