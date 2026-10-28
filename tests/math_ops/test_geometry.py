import pytest

from src.math_ops import rectangle_area_perimeter, triangle_type


@pytest.mark.parametrize(
    "length, width, expected",
    [
        (5.0, 3.0, (15.0, 16.0)),
        (10.0, 10.0, (100.0, 40.0)),
        (7.5, 2.0, (15.0, 19.0)),
        (1.0, 1.0, (1.0, 4.0)),
        (0.0, 5.0, (0.0, 10.0)),
        (0.0, 0.0, (0.0, 0.0)),
        (2.5, 4.0, (10.0, 13.0)),
        (100.0, 1.0, (100.0, 202.0)),
        (3.3, 2.2, (7.26, 11.0)),
        (12.5, 8.5, (106.25, 42.0)),
    ],
)
def test_rectangle_area_perimeter(
    length: float,
    width: float,
    expected: tuple[float, float],
) -> None:
    assert rectangle_area_perimeter(length, width) == pytest.approx(expected)


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (3.0, 3.0, 3.0, "Equilateral"),
        (5.0, 5.0, 5.0, "Equilateral"),
        (1.0, 1.0, 1.0, "Equilateral"),
        (3.0, 3.0, 5.0, "Isosceles"),
        (5.0, 5.0, 3.0, "Isosceles"),
        (3.0, 5.0, 3.0, "Isosceles"),
        (3.0, 4.0, 5.0, "Scalene"),
        (6.0, 7.0, 8.0, "Scalene"),
        (2.5, 3.5, 4.5, "Scalene"),
        (1.0, 2.0, 3.0, "Invalid"),
        (1.0, 2.0, 4.0, "Invalid"),
        (5.0, 1.0, 2.0, "Invalid"),
        (3.0, 3.0, 6.0, "Invalid"),
        (0.0, 3.0, 3.0, "Invalid"),
        (0.0, 0.0, 0.0, "Invalid"),
        (-3.0, 4.0, 5.0, "Invalid"),
    ],
)
def test_triangle_type(
    a: float,
    b: float,
    c: float,
    expected: str,
) -> None:
    assert triangle_type(a, b, c) == expected
