import pytest

from src.math_ops import gcd, lcm


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (12, 8, 4),
        (8, 12, 4),
        (17, 5, 1),
        (5, 17, 1),
        (100, 75, 25),
        (7, 7, 7),
        (1, 1, 1),
        (1, 10, 1),
        (0, 5, 5),
        (5, 0, 5),
        (0, 0, 0),
        (48, 18, 6),
        (270, 192, 6),
        (-12, 8, 4),
        (12, -8, 4),
        (-12, -8, 4),
    ],
)
def test_gcd(a: int, b: int, expected: int) -> None:
    assert gcd(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (12, 8, 24),
        (8, 12, 24),
        (17, 5, 85),
        (5, 17, 85),
        (100, 75, 300),
        (7, 7, 7),
        (1, 1, 1),
        (1, 10, 10),
        (0, 5, 0),
        (5, 0, 0),
        (0, 0, 0),
        (48, 18, 144),
        (270, 192, 8640),
        (-12, 8, 24),
        (12, -8, 24),
        (-12, -8, 24),
    ],
)
def test_lcm(a: int, b: int, expected: int) -> None:
    assert lcm(a, b) == expected
