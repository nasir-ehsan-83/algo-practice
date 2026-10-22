import pytest

from src.math_ops import is_even


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
