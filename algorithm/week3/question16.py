def fibonacci(n: int) -> list[int]:
    if n <= 0:
        return [];

    seq: list[int] = [0];

    if n == 1:
        return seq;

    seq.append(1);

    for i in range(2, n):
        seq.append(seq[i - 1] + seq[i - 2]);
    
    return seq;