import pytest

from src.math_ops import is_even, max_of_three


@pytest.mark.parametrize(
    "number, expected",
    [
        (2, True),
        (0, True),
        (16, True),
        (38, True),
        (104, True),
        (93, False),
        (17, False),
        (55, False),
        (-2, True),
        (-16, True),
        (-38, True),
        (-104, True),
        (2.0, True),
        (0.0, True),
        (16.2, False),
        (38.3, False),
        (10.4, False),
        (-2.1, False),
        (-16.0, True),
        (-3.8, False),
        (-10.4, False),
    ],
)
def test_is_even(number: float, expected: bool) -> None:
    assert is_even(number) == expected


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (1, 2, 3, 3),
        (10, 17, 13, 17),
        (20, 17, 13, 20),
        (3, 3, 3, 3),
        (0, 0, 0, 0),
        (-2, -1, -3, -1),
        (-10, -17, -13, -10),
        (-20, -17, -13, -13),
        (-3, -3, -3, -3),
        (11.2, 12.3, 13.0, 13.0),
        (10.1, 17.2, 13.4, 17.2),
        (20.1, 17.2, 13.3, 20.1),
        (3.0, 3.0, 3.0, 3.0),
        (0.0, 0.1, 0.2, 0.2),
        ("a", "b", "d", "d"),
        ("f", "b", "c", "f"),
        ("h", "g", "e", "h"),
        ("e", "i", "a", "i"),
        ("u", "o", "s", "u"),
        ("ali", "ahmad", "akbar", "ali"),
        ("basir", "ali", "omer", "omer"),
    ],
)
def test_max_of_three[T: (int, float, str)](a: T, b: T, c: T, expected: T) -> None:
    assert max_of_three(a, b, c) == expected
