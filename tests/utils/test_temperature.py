import pytest

from src.utils import cel_to_fah, fah_to_cel


@pytest.mark.parametrize(
    "c, expected",
    [
        (0, 32),
        (100, 212),
        (25, 77),
        (37, 98.6),
        (-40, -40),
        (-10, 14),
        (10.5, 50.9),
    ],
)
def test_cel_to_fah(c: float, expected: float) -> None:
    assert cel_to_fah(c) == pytest.approx(expected)


@pytest.mark.parametrize(
    "f, expected",
    [
        (32, 0),
        (212, 100),
        (77, 25),
        (98.6, 37),
        (-40, -40),
        (14, -10),
        (50.9, 10.5),
    ],
)
def test_fah_to_cel(f: float, expected: float) -> None:
    assert fah_to_cel(f) == pytest.approx(expected)
