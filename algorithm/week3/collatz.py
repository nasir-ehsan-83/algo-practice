def collatz_sequence(n: int) -> tuple[list[int], int]:
    seq: list[int] = [n]
    steps: int = 0

    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

        seq.append(n)
        steps += 1

    return seq, steps
