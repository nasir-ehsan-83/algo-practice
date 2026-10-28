import pytest

from src.math_ops import decimal_to_binary, gcd, lcm, primes_up_to


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


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, []),
        (1, []),
        (2, [2]),
        (3, [2, 3]),
        (4, [2, 3]),
        (5, [2, 3, 5]),
        (10, [2, 3, 5, 7]),
        (11, [2, 3, 5, 7, 11]),
        (13, [2, 3, 5, 7, 11, 13]),
        (20, [2, 3, 5, 7, 11, 13, 17, 19]),
        (25, [2, 3, 5, 7, 11, 13, 17, 19, 23]),
        (30, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]),
        (50, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]),
        (
            100,
            [
                2,
                3,
                5,
                7,
                11,
                13,
                17,
                19,
                23,
                29,
                31,
                37,
                41,
                43,
                47,
                53,
                59,
                61,
                67,
                71,
                73,
                79,
                83,
                89,
                97,
            ],
        ),
        (-5, []),
    ],
)
def test_primes_up_to(n: int, expected: list[int]) -> None:
    assert primes_up_to(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, "0b0"),
        (1, "0b1"),
        (2, "0b10"),
        (3, "0b11"),
        (4, "0b100"),
        (5, "0b101"),
        (8, "0b1000"),
        (10, "0b1010"),
        (15, "0b1111"),
        (16, "0b10000"),
        (255, "0b11111111"),
        (1024, "0b10000000000"),
        (-1, "-0b1"),
        (-5, "-0b101"),
        (-10, "-0b1010"),
    ],
)
def test_decimal_to_binary(n: int, expected: str) -> None:
    assert decimal_to_binary(n) == expected
