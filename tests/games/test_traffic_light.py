import pytest

from src.games import traffic_light


@pytest.mark.parametrize(
    "color, expected",
    [
        ("Red", "Stop"),
        ("Yellow", "Ready"),
        ("Green", "Go"),
        ("Blue", "Invalid"),
        ("red", "Invalid"),
        ("", "Invalid"),
    ],
)
def test_traffic_light(color: str, expected: str) -> None:
    assert traffic_light(color) == expected
