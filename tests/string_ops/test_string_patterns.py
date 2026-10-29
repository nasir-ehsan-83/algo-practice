import pytest

from src.string_ops import pattern_match


@pytest.mark.parametrize(
    "pattern, s, expected",
    [
        ("abba", "dog cat cat dog", True),
        ("abba", "dog cat cat fish", False),
        ("aaaa", "dog cat cat dog", False),
        ("abc", "dog cat fish", True),
        ("abc", "dog dog dog", False),
        ("ab", "dog cat", True),
        ("ab", "dog dog", False),
        ("", "", True),
        ("a", "", False),
        ("", "dog", False),
        ("ab", "dog cat fish", False),
        ("aaa", "dog dog dog", True),
        ("abc", "dog cat dog", False),
    ],
)
def test_pattern_match(
    pattern: str,
    s: str,
    expected: bool,
) -> None:
    assert pattern_match(pattern, s) is expected
