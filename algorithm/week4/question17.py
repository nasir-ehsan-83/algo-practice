def abbreviate_sentence(sentence: str) -> str:
    words: list[str] = sentence.split();
    return ' '.join(word[0] for word in words if word);
