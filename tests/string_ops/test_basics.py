import pytest

from src.string_ops import char_freq, count_vowels, reverse_string


@pytest.mark.parametrize(
    "s, expected",
    [
        ("hello", "olleh"),
        ("Python", "nohtyP"),
        ("a", "a"),
        ("", ""),
        ("hello world", "dlrow olleh"),
        ("12345", "54321"),
    ],
)
def test_reverse_string(s: str, expected: str) -> None:
    assert reverse_string(s) == expected


@pytest.mark.parametrize(
    "s, expected",
    [
        ("hello", 2),
        ("AEIOU", 5),
        ("Python", 1),
        ("rhythm", 0),
        ("", 0),
        ("Hello World", 3),
        ("aAeEiIoOuU", 10),
        ("12345", 0),
    ],
)
def test_count_vowels(s: str, expected: int) -> None:
    assert count_vowels(s) == expected


@pytest.mark.parametrize(
    "s, expected",
    [
        ("hello", {"h": 1, "e": 1, "l": 2, "o": 1}),
        ("aaa", {"a": 3}),
        ("", {}),
        ("aAbA", {"a": 1, "A": 2, "b": 1}),
        (
            "hello world",
            {
                "h": 1,
                "e": 1,
                "l": 3,
                "o": 2,
                " ": 1,
                "w": 1,
                "r": 1,
                "d": 1,
            },
        ),
        ("112233", {"1": 2, "2": 2, "3": 2}),
    ],
)
def test_char_freq(s: str, expected: dict[str, int]) -> None:
    assert char_freq(s) == expected
