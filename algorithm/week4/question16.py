def multiply_matrix[T: (int, float)](A: list[list[T]], B: list[list[T]]):
    rows_A: int = len(A);
    cols_A: int = len(A[0]);
    rows_B: int = len(B); 
    cols_B: int = len(B[0]);

    if cols_A != rows_B:
        return None;

    result: list[list[int]] = [[0 for _ in range(cols_B)] for _ in range(rows_A)];

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j];
    
    return result;