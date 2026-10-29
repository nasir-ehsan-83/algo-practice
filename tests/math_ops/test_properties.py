import pytest

from src.math_ops import number_type


@pytest.mark.parametrize(
    "number, expected",
    [
        (123, "Positive"),
        (65, "Positive"),
        (0.5, "Positive"),
        (3, "Positive"),
        (-123, "Negative"),
        (-12, "Negative"),
        (-0.5, "Negative"),
        (0, "Zero"),
        (0.0, "Zero"),
    ],
)
def test_number_type(number: float, expected: str) -> None:
    assert number_type(number) == expected
