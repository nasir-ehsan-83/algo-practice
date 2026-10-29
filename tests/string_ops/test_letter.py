import pytest

from src.string_ops import letter_type


@pytest.mark.parametrize(
    "c, expected",
    [
        ("a", "Vowel"),
        ("e", "Vowel"),
        ("i", "Vowel"),
        ("o", "Vowel"),
        ("u", "Vowel"),
        ("A", "Vowel"),
        ("E", "Vowel"),
        ("b", "Consonant"),
        ("Z", "Consonant"),
        ("5", "Digit"),
        ("0", "Digit"),
        ("@", "Special"),
        (" ", "Special"),
        ("!", "Special"),
    ],
)
def test_letter_type(c: str, expected: str) -> None:
    assert letter_type(c) == expected
