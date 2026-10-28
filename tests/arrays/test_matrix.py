import pytest

from src.arrays import multiply_matrix


@pytest.mark.parametrize(
    "A, B, expected",
    [
        (
            [[1, 2], [3, 4]],
            [[5, 6], [7, 8]],
            [[19, 22], [43, 50]],
        ),
        (
            [[1, 2, 3]],
            [[4], [5], [6]],
            [[32]],
        ),
        (
            [[1], [2], [3]],
            [[4, 5, 6]],
            [[4, 5, 6], [8, 10, 12], [12, 15, 18]],
        ),
        (
            [[1, 0], [0, 1]],
            [[7, 8], [9, 10]],
            [[7, 8], [9, 10]],
        ),
        (
            [[0, 0], [0, 0]],
            [[1, 2], [3, 4]],
            [[0, 0], [0, 0]],
        ),
        (
            [[1, 2, 3], [4, 5, 6]],
            [[7, 8], [9, 10], [11, 12]],
            [[58, 64], [139, 154]],
        ),
    ],
)
def test_multiply_matrix(
    A: list[list[int]],
    B: list[list[int]],
    expected: list[list[int]],
) -> None:
    assert multiply_matrix(A, B) == expected


def test_multiply_matrix_incompatible_dimensions() -> None:
    A = [[1, 2, 3]]
    B = [[1, 2], [3, 4]]
    assert multiply_matrix(A, B) is None


def test_multiply_matrix_empty() -> None:
    assert multiply_matrix([], []) is None
