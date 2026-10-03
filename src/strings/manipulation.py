def compress_string(s: str) -> str:
    if not s:
        return ""

    result: str = ""
    count: int = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1

        else:
            result += s[i - 1] + str(count)
            count = 1

    result += s[-1] + str(count)
    return result


def abbreviate_sentence(sentence: str) -> str:
    words: list[str] = sentence.split()

    return " ".join(word[0] for word in words if word)
