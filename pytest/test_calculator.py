from calculator import Calculator
# import pytest

def test_addition(calculator):
    assert calculator.addition(2, 6) == 8
    assert calculator.addition(0, 0) == 0
    assert calculator.addition(-1, 1) == 0
    assert calculator.addition(-5, -3) == -8

def test_subtraction(calculator):
    assert calculator.subtraction(10, 5) == 5
    assert calculator.subtraction(0, 0) == 0
    assert calculator.subtraction(-1, -1) == 0
    assert calculator.subtraction(-5, -3) == -2

def test_multiplication(calculator):
    assert calculator.multiplication(4, 2) == 8
    assert calculator.multiplication(0, 5) == 0
    assert calculator.multiplication(-1, 1) == -1
    assert calculator.multiplication(-3, -3) == 9

def test_division(calculator):
    assert calculator.division(8, 2) == 4
    assert calculator.division(-6, 2) == -3
    assert calculator.division(-9, -3) == 3
    try:
        result = calculator.division(5, 0)
    except ZeroDivisionError:
        result = None
    assert result is None

def test_loop_sum():
    numbers = [1, 3, 5, 18, 9]
    total = 0
    for number in numbers:
        total += number
    assert total == 36

def test_loop_art():
    rows = 5
    art = []
    start = 0
    while start < rows:
        spaces = " " * (rows - start - 1)
        stars = "*" * (2 * start + 1)
        art.append(spaces + stars)
        start += 1
    expected_art = [
        "    *",
        "   ***",
        "  *****",
        " *******",
        "*********"
    ]
    assert art == expected_art

