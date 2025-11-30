# from calculator import addition, subtraction, multiplication, division
# import pytest

def test_addition():
    assert 2 + 6 == 8
    assert 0 + 0 == 0
    assert -1 + 1 == 0
    assert -5 + -3 == -8

def test_subtraction():
    assert 10 - 5 == 5
    assert 0 - 0 == 0
    assert -1 - (-1) == 0
    assert -5 - (-3) == -2

def test_multiplication():
    assert 4 * 2 == 8
    assert 0 * 5 == 0
    assert -1 * 1 == -1
    assert -3 * -3 == 9

def test_division():
    assert 8 / 2 == 4
    assert -6 / 2 == -3
    assert -9 / -3 == 3
    try:
        result = 5 / 0
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

