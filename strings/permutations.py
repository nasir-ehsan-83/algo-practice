def string_permutations(s: str) -> list[str]:
    if len(s) <= 1:
        return [s]

    perms: list[str] = []

    for i, ch in enumerate(s):
        for perm in string_permutations(s[:i] + s[i + 1 :]):
            perms.append(ch + perm)

    return perms


def longest_palindrome(s: str) -> str:
    n: int = len(s)

    if n == 0:
        return ""

    start: int = 0
    max_len: int = 1

    for i in range(n):
        # odd length
        l: int = i
        r: int = i

        while l >= 0 and r < n and s[l] == s[r]:
            if (r - l + 1) > max_len:
                start = l
                max_len = r - l + 1

            l -= 1
            r += 1

        # even length
        l = i
        r = i + 1

        while l >= 0 and r < n and s[l] == s[r]:
            if (r - l + 1) > max_len:
                start, max_len = l, (r - l + 1)

            l -= 1
            r += 1

    return s[start : start + max_len]
