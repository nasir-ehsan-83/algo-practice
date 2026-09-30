def pascal_triangle(rows: int) -> list[list[int]]:
    result: list[list[int]] = []

    for i in range(rows):
        row: list[int] = [1] * (i + 1)

        for j in range(1, i):
            row[j] = result[i - 1][j - 1] + result[i - 1][j]

        result.append(row)

    return result
