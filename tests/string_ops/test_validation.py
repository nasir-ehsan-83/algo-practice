import pytest

from src.string_ops import is_balanced, password_strength


@pytest.mark.parametrize(
    "password, expected",
    [
        ("", "Weak"),
        ("abc", "Weak"),
        ("Abc123", "Weak"),
        ("Abcdefgh", "Weak"),
        ("abcdefgh1", "Weak"),
        ("ABCDEFGH1", "Weak"),
        ("Abcdef12", "Strong"),
        ("Password123", "Strong"),
        ("A1bcdefg", "Strong"),
        ("Abc123!@", "Strong"),
    ],
)
def test_password_strength(password: str, expected: str) -> None:
    assert password_strength(password) == expected


@pytest.mark.parametrize(
    "s, expected",
    [
        ("", True),
        ("()", True),
        ("{}", True),
        ("[]", True),
        ("(){}[]", True),
        ("({[]})", True),
        ("((()))", True),
        ("([]{})", True),
        ("(", False),
        (")", False),
        ("(]", False),
        ("([)]", False),
        ("{[}", False),
        ("((()", False),
        ("())", False),
        ("abc", True),
        ("a(b)c", True),
        ("{a[ b ]}", True),
    ],
)
def test_is_balanced(s: str, expected: bool) -> None:
    assert is_balanced(s) is expected
