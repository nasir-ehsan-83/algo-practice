import pytest

from src.math_ops import add_numbers, simple_interest, swap
from src.math_ops import power as power_func


@pytest.mark.parametrize(
    "first_num, second_num, expected",
    [
        (0, 0, 0),
        (12, 3, 15),
        (12, -3, 9),
        (-13, -7, -20),
        (-13.3, -7.2, -20.5),
        (13.3, 10.2, 23.5),
        (True, False, 1),
        (False, False, 0),
        (True, True, 2),
        ("2", "3", 5),
        ("2.7", "3.3", 6),
        ("-27", "3", -24),
        ("-27", "-3", -30),
        ("-27", "27", 0),
        ("0", "0", 0),
    ],
)
def test_add_numbers[T: (int | float)](
    first_num: T, second_num: T, expected: T
) -> None:
    assert add_numbers(first_num, second_num) == expected

    with pytest.raises(ValueError):
        add_numbers(True, None)  # type: ignore
    with pytest.raises(ValueError):
        add_numbers(1, None)  # type: ignore
    with pytest.raises(ValueError):
        add_numbers(34, "None")  # type: ignore
    with pytest.raises(ValueError):
        add_numbers("True", "None")  # type: ignore


@pytest.mark.parametrize(
    "first, second, expected",
    [
        (4, 5, (5, 4)),
        (-43, -51, (-51, -43)),
        (13.4, 56.0, (56.0, 13.4)),
        ("a", "b", ("b", "a")),
        ("ali", "ahmad", ("ahmad", "ali")),
        (True, False, (False, True)),
        (None, True, (True, None)),
        ([5, 6, 7, 8], [1, 2, 3, 4], ([1, 2, 3, 4], [5, 6, 7, 8])),
    ],
)
def test_swap[T](first: T, second: T, expected: tuple[T, T]) -> None:
    assert swap(first, second) == expected


@pytest.mark.parametrize(
    "base, power, expected",
    [
        (2, 3, 8),
        (-5, 2, 25),
        (-3, 3, -27),
        (1.2, 3, 1.728),
        (-1.2, 3, -1.728),
        (3.2, 2, 10.240000000000002),
        (-3.2, 2, 10.240000000000002),
    ],
)
def test_power(base: float, power: int, expected: float) -> None:
    assert power_func(base, power) == expected


@pytest.mark.parametrize(
    "p, r, t, expected",
    [
        (1000.0, 5.0, 2, 100.0),
        (5000.0, 10.0, 3, 1500.0),
        (2000.0, 7.5, 4, 600.0),
        (100.0, 1.0, 1, 1.0),
        (10000.0, 12.5, 5, 6250.0),
        (0.0, 5.0, 2, 0.0),
        (1000.0, 0.0, 2, 0.0),
        (1000.0, 5.0, 0, 0.0),
        (1500.0, 4.0, 2, 120.0),
    ],
)
def test_simple_interest(
    p: float,
    r: float,
    t: int,
    expected: float,
) -> None:
    assert simple_interest(p, r, t) == pytest.approx(expected)
