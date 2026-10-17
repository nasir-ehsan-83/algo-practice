import pytest

from src.math_ops import add_numbers


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
