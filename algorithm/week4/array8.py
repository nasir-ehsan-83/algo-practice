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
