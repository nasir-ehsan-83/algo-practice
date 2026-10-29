import pytest

from src.string_ops import abbreviate_sentence, compress_string


@pytest.mark.parametrize(
    "s, expected",
    [
        ("aaabbc", "a3b2c1"),
        ("abcd", "a1b1c1d1"),
        ("aaaa", "a4"),
        ("a", "a1"),
        ("", ""),
        ("aa  bb", "a2 2b2"),
        ("11122", "1322"),
    ],
)
def test_compress_string(s: str, expected: str) -> None:
    assert compress_string(s) == expected


@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("hello world", "hw"),
        ("Python is awesome", "Pia"),
        ("", ""),
        ("hello", "h"),
        ("  hello   world  ", "hw"),
        ("Artificial Intelligence", "AI"),
        ("one two three", "ott"),
        ("123 abc", "1a"),
    ],
)
def test_abbreviate_sentence(sentence: str, expected: str) -> None:
    assert abbreviate_sentence(sentence) == expected
