from unittest.mock import patch

import pytest

from src.games import rock_paper


@pytest.mark.parametrize(
    "player_choice, computer_choice, expected",
    [
        ("rock", "rock", "Draw"),
        ("paper", "paper", "Draw"),
        ("scissors", "scissors", "Draw"),
        ("rock", "scissors", "Player wins"),
        ("paper", "rock", "Player wins"),
        ("scissors", "paper", "Player wins"),
        ("rock", "paper", "Computer wins"),
        ("paper", "scissors", "Computer wins"),
        ("scissors", "rock", "Computer wins"),
    ],
)
def test_rock_paper_scissors(
    player_choice: str,
    computer_choice: str,
    expected: str,
) -> None:
    with patch.object(
        rock_paper.random,
        "choice",
        return_value=computer_choice,
    ):
        assert rock_paper.rock_paper_scissors(player_choice) == expected
