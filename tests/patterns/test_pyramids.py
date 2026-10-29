import pytest

from src.patterns import (
    multiplication_table,
    pascal_triangle,
    pyramid,
    right_aligned_triangle,
    right_triangle,
)


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, ["*"]),
        (2, [" *", "***"]),
        (3, ["  *", " ***", "*****"]),
        (0, []),
    ],
)
def test_pyramid(n: int, expected: list[str]) -> None:
    assert pyramid(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, ["*"]),
        (2, ["*", "**"]),
        (3, ["*", "**", "***"]),
        (0, []),
    ],
)
def test_right_triangle(n: int, expected: list[str]) -> None:
    assert right_triangle(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, ["*"]),
        (2, [" *", "**"]),
        (3, ["  *", " **", "***"]),
        (0, []),
    ],
)
def test_right_aligned_triangle(n: int, expected: list[str]) -> None:
    assert right_aligned_triangle(n) == expected


@pytest.mark.parametrize(
    "rows, expected",
    [
        (0, []),
        (1, [[1]]),
        (2, [[1], [1, 1]]),
        (3, [[1], [1, 1], [1, 2, 1]]),
        (4, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]),
    ],
)
def test_pascal_triangle(rows: int, expected: list[list[int]]) -> None:
    assert pascal_triangle(rows) == expected


@pytest.mark.parametrize(
    "n, upto, expected",
    [
        (2, 3, [(2, 1, 2), (2, 2, 4), (2, 3, 6)]),
        (5, 2, [(5, 1, 5), (5, 2, 10)]),
        (7, 1, [(7, 1, 7)]),
        (3, 0, []),
    ],
)
def test_multiplication_table(
    n: int,
    upto: int,
    expected: list[tuple[int, int, int]],
) -> None:
    assert multiplication_table(n, upto) == expected


def test_multiplication_table_default_upto() -> None:
    result = multiplication_table(3)

    assert len(result) == 10
    assert result[0] == (3, 1, 3)
    assert result[-1] == (3, 10, 30)
