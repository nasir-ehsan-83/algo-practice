import pytest

from src.math_ops import rectangle_area_perimeter


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
