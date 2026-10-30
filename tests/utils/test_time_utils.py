import pytest

from src.utils import is_leap_year, month_info, seconds_to_hms


@pytest.mark.parametrize(
    "year, expected",
    [
        (2024, True),
        (2020, True),
        (2000, True),
        (1900, False),
        (2023, False),
        (2025, False),
        (2100, False),
        (2400, True),
        (1, False),
    ],
)
def test_is_leap_year(year: int, expected: bool) -> None:
    assert is_leap_year(year) is expected


@pytest.mark.parametrize(
    "month, expected",
    [
        (1, ("January", 31)),
        (2, ("February", 28)),
        (3, ("March", 31)),
        (4, ("April", 30)),
        (5, ("May", 31)),
        (6, ("June", 30)),
        (7, ("July", 31)),
        (8, ("August", 31)),
        (9, ("September", 30)),
        (10, ("October", 31)),
        (11, ("November", 30)),
        (12, ("December", 31)),
        (0, ("Invalid", 0)),
        (13, ("Invalid", 0)),
        (-1, ("Invalid", 0)),
    ],
)
def test_month_info(month: int, expected: tuple[str, int]) -> None:
    assert month_info(month) == expected


@pytest.mark.parametrize(
    "seconds, expected",
    [
        (0, (0, 0, 0)),
        (1, (0, 0, 1)),
        (59, (0, 0, 59)),
        (60, (0, 1, 0)),
        (90, (0, 1, 30)),
        (3599, (0, 59, 59)),
        (3600, (1, 0, 0)),
        (3661, (1, 1, 1)),
        (7200, (2, 0, 0)),
        (86400, (24, 0, 0)),
        (90061, (25, 1, 1)),
    ],
)
def test_seconds_to_hms(
    seconds: int,
    expected: tuple[int, int, int],
) -> None:
    assert seconds_to_hms(seconds) == expected
