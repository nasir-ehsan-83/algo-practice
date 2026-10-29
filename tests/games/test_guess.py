import pytest

from src.games import guess_number


@pytest.mark.parametrize(
    "secret, guess, expected",
    [
        (5, 5, "Correct"),
        (10, 10, "Correct"),
        (1, 1, "Correct"),
        (5, 3, "Too Low"),
        (10, 1, "Too Low"),
        (100, 50, "Too Low"),
        (5, 7, "Too High"),
        (10, 15, "Too High"),
        (1, 100, "Too High"),
        (0, 0, "Correct"),
        (-5, -5, "Correct"),
        (-5, -10, "Too Low"),
        (-5, 0, "Too High"),
    ],
)
def test_guess_number(
    secret: int,
    guess: int,
    expected: str,
) -> None:
    assert guess_number(secret, guess) == expected
