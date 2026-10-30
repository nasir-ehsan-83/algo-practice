import pytest

from src.utils import grade


@pytest.mark.parametrize(
    "marks, expected",
    [
        (100, "A"),
        (95, "A"),
        (90, "A"),
        (89, "B"),
        (85, "B"),
        (80, "B"),
        (79, "C"),
        (75, "C"),
        (70, "C"),
        (69, "D"),
        (65, "D"),
        (60, "D"),
        (59, "F"),
        (50, "F"),
        (0, "F"),
        (-5, "F"),
    ],
)
def test_grade(marks: float, expected: str) -> None:
    assert grade(marks) == expected
