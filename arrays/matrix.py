def multiply_matrix(A: list[list[int]], B: list[list[int]]):
    rows_A: int = len(A)
    cols_A: int = len(A[0])
    rows_B: int = len(B)
    cols_B: int = len(B[0])

    if cols_A != rows_B:
        return None

    result: list[list[int]] = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result


def set_zeroes[T](matrix: list[list[T]]) -> None | list[list[T]]:
    if not matrix:
        return

    rows: int = len(matrix)
    cols: int = len(matrix[0])
    row_flags: list[bool] = [False] * rows
    col_flags: list[bool] = [False] * cols

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                row_flags[i] = True
                col_flags[j] = True

    for i in range(rows):
        for j in range(cols):
            if row_flags[i] or col_flags[j]:
                matrix[i][j] = 0

    return matrix
