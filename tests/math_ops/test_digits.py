import pytest

from src.math_ops import reverse_number


@pytest.mark.parametrize(
    "number, expected",
    [
        (1, 1),
        (12, 21),
        (54, 45),
        (5, 5),
        (111, 111),
        (789, 987),
        (0, 0),
        (3567, 7653),
        (222, 222),
    ],
)
def test_reverse_number(number: int, expected: int) -> None:
    assert reverse_number(number) == expected
