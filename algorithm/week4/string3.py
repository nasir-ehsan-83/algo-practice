def string_permutations(s: str) -> list[str]:
    if len(s) <= 1:
        return [s]

    perms: list[str] = []

    for i, ch in enumerate(s):
        for perm in string_permutations(s[:i] + s[i + 1 :]):
            perms.append(ch + perm)

    return perms
