import pytest

from src.string_ops import longest_palindrome, string_permutations


@pytest.mark.parametrize(
    "s, expected",
    [
        ("a", ["a"]),
        ("ab", ["ab", "ba"]),
        ("abc", ["abc", "acb", "bac", "bca", "cab", "cba"]),
        ("", [""]),
        ("aa", ["aa", "aa"]),
    ],
)
def test_string_permutations(s: str, expected: list[str]) -> None:
    assert string_permutations(s) == expected


@pytest.mark.parametrize(
    "s, expected",
    [
        ("", ""),
        ("a", "a"),
        ("babad", "bab"),
        ("cbbd", "bb"),
        ("racecar", "racecar"),
        ("abba", "abba"),
        ("abc", "a"),
        ("aaaa", "aaaa"),
        ("abccba", "abccba"),
    ],
)
def test_longest_palindrome(s: str, expected: str) -> None:
    assert longest_palindrome(s) == expected
