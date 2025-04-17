# Calculator Programming Challenge

For this challenge, you'll create a Python script that will accept user input
of a mathematical expression in prefix notation \(also known as
[Polish Notation](https://en.wikipedia.org/wiki/Polish_notation)\) and output
what that expression evaluates to.

## Setup

The tests in this challenge require some dependencies. To set up, navigate to the
directory this file is in on your terminal and run
`pip install -r ./requirements.txt`.

## Task

You can choose to write your own code from scratch, but the tests set up assume
that you use the following functions:

```py
# Takes a list of tokens produced by `tokenize_expression`
# and evaluates them to produce a result. Returns that
# result.
# 
# See README.md for resources for how this can be 
# implemented.
def evaluate_tokens(tokens: list) -> float:

# Takes an expression stored in `expr` and returns a
# list containing each token in that expression.
# 
# Example: 
# INPUT: "+ 1 * 4 / 7 + 1 3" 
# OUTPUT: ["+", "1", "*", "4", "/", "7", "+", "1", "3"] 
def tokenize_expression(expr: str) -> list:
```

### `tokenize_expression(expr: string) -> list`

This should be fairly easy to implement with basic string manipulation. You need to
take the string provided to you and split it into "tokens", each token being a
substrings of the provided string, separated by white spaces. 

### `evaluate_tokens(tokens: list) -> float`

This function takes in the list of tokens and returns the final value the expression
evaluates to.

The input consists of one `expression` surrounded by any number of spaces. An
`expression` can be defined as the following:

An `expression` is either:
1. An `operator`, followed by a space, a `sub-expression`, a space, and another
`sub-expression`; or
2. A single `operand` 

```
expression = operator SP sub-expression SP sub-expression
             / operand
```

A `sub-expression` is the same thing as a regular `expression`, it's used above under
that name just for clarity.

```
sub-expression = expression
```

An `operator` is any of `+`, `-`, `*`, or `/`

```
operator = "+" / "-" / "*" / "/"
```

An `operand` is one or more digits (`1*<something>` means "one or more of".
`1*3<something>` would mean between one and three of)

```
operand = 1*DIGIT
```

`SP` is used to mean "one or more spaces"

```
SP = 1*" "
```

There are two general ways you can approach this:

#### Recursive Approach

For the recursive approach, you recursively attempt to parse smaller and smaller
sub-lists until you reach a trivial case that is easy to program (the "base case").

Think about what the base case should be. How many tokens would your base case
have? Is it possible to divide it any further to create an even simpler case?

#### Stack Based Approach

For the stack based approach, you would first reverse the list to get
[Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation)
\(with the operands reversed\)then you would go through the tokens one by one.
If the token you encounter is an operand, you push it onto a stack. If the token
you encounter is an operator, you pop two elements from the stack, apply the
operation, then push the result back onto the stack.

When you are done going through the input tokens, your stack should consist of a
single number. You would return that number.

Keep in mind that when you reverse the tokens, you also switch the order of the
operands. You must keep this in mind to avoid incorrect results.

For example:

1. Algebraic Notation: `1 / 12`
2. Polish Notation: `/ 1 12`
3. Polish Notation, with the tokens reversed: `12 1 /`
4. Actual Reverse Polish Notation (RPN): `1 12 /`

Note how (3) above, if interpreted as RPN, would be `12 / 1`, not `1 / 12`. 

## Helper Functions

Some helper functions are provided to make implementation easier.

```py
# Helper function that returns the result of the operation
# requested.
# 
# This has been implemented for you, you don't need to 
# modify it.
# 
# Returns [op1] [operand] [op2]
def apply_operation(op1: float, op2: float, operand: str) -> float:

# Helper function that returns true if the given string is
# a valid operator.
# 
# This has been implemented for you, you don't need to 
# modify it.
def is_operator(token: string) -> bool:

# Helper function that returns true if the given string is
# a valid operand.
# 
# This has been implemented for you, you don't need to 
# modify it.
def is_operand(token: string) -> bool:
```

### `apply_operator(op1: float, op2: float, operand: str) -> float`

This function returns \[op1\] \[operand\] \[op2\]. For example,
`apply_operator(10,2,'/')` would return `5`.

### `is_operator(token: str) -> bool`

Returns `True` if the provided token is a valid operator, `False` if not.

### `is_operand(token: str) -> bool`

Returns `True` if the provided token is a valid operand, `False` if not.

## Testing

There are tests provided which you can run by typing `pytest -v` into your console.
They are designed to be passed in order as you make progress.

These tests are:

1. tokenize_simple
2. tokenize_multiple_spaces
3. tokenize_empty_string
4. evaluate_simple
5. evaluate_harder
6. evaluate_operand_order
7. end_to_end

