def reverse_string(s: str) -> str:
    reversed_str: str = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]

    return reversed_str


def count_vowels(s: str) -> int:
    vowels: str = "aeiouAEIOU"
    count: int = 0

    for char in s:
        if char in vowels:
            count += 1

    return count


def char_freq(s: str) -> dict[str, int]:
    freq: dict[str, int] = {}

    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    return freq
