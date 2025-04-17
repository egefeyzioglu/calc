#!/usr/bin/env python3

import re

# Helper function that returns true if the given string is
# a valid operator.
# 
# This has been implemented for you, you don't need to 
# modify it.
def is_operator(token: str) -> bool:
    return re.search("^[\\+\\-\\/\\*\\^]$", token) != None

# Helper function that returns true if the given string is
# a valid operand.
# 
# This has been implemented for you, you don't need to 
# modify it.
def is_operand(token: str) -> bool:
    return re.search("^[0-9]+$", token) != None

# Helper function that returns the result of the operation
# requested.
# 
# This has been implemented for you, you don't need to 
# modify it.
# 
# Returns [op1] [operand] [op2]
def apply_operation(op1: float, op2: float, operand: str) -> float:
    if not isinstance(op1, float):
        raise ValueError(f"Expected first operand of type float, got {type(op1)}")
    if not isinstance(op2, float):
        raise ValueError(f"Expected second operand of type float, got {type(op2)}")
    if not isinstance(operand, str) or len(operand) != 1:
        raise ValueError(f"Expected operator of type string and len 1, got {type(operand)} or len {len(operand)}: \"{operand}\"")
    if operand == "+":
        return op1 + op2
    elif operand == "-":
        return op1 - op2
    elif operand == "*":
        return op1 * op2
    elif operand == "/":
        return op1 / op2
    else:
        raise ValueError(f"Illegal operand {operand}")

# Takes a list of tokens produced by `tokenize_expression`
# and evaluates them to produce a result. Returns that
# result.
# 
# See README.md for resources about how this can be 
# implemented.
def evaluate_tokens(tokens: list) -> float:
    pass


# Takes an expression stored in `expr` and returns a
# list containing each token in that expression.
# 
# Example: 
# INPUT: "+ 1 * 4 / 7 + 1 3" 
# OUTPUT: ["+", "1", "*", "4", "/", "7", "+", "1", "3"] 
def tokenize_expression(expr: str) -> list:
    pass

# This is the main function that does the input/output
# from the user and calls the functions you implemented
# above.
# 
# This has been implemented for you, you don't need to 
# modify it.
def main():
    while True:
        try:
            expr = input("Enter expression to be evaluated (or Ctrl + D to exit)\n> ")
            tokens = tokenize_expression(expr)
            result = evaluate_tokens(tokens)
            print(result);
        except EOFError:
            print()
            exit(0)

if __name__ == "__main__":
    main()

