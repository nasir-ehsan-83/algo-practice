def rearrange_even_odd(arr: list[int]) -> list[int]:
    evens: list[int] = []
    odds: list[int] = []

    for num in arr:
        if num % 2 == 0:
            evens.append(num)

        else:
            odds.append(num)

    return evens + odds
