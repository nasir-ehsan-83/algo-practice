import pytest

from src.utils import bmi_calculator


@pytest.mark.parametrize(
    "weight, height, expected",
    [
        (50, 1.70, (17.30, "Underweight")),
        (60, 1.70, (20.76, "Normal weight")),
        (75, 1.70, (25.95, "Overweight")),
        (90, 1.70, (31.14, "Obese")),
        (53.465, 1.70, (18.50, "Normal weight")),
        (72.25, 1.70, (25.00, "Overweight")),
        (86.7, 1.70, (30.00, "Obese")),
    ],
)
def test_bmi_calculator(
    weight: float,
    height: float,
    expected: tuple[float, str],
) -> None:
    assert bmi_calculator(weight, height) == expected
