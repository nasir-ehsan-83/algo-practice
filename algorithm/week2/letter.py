type char = str


def letter_type(c: char) -> str:
    vowels: str = "aeiouAEIOU"
    if c.isdigit():
        return "Digit"
    elif c in vowels:
        return "Vowel"
    elif c.isalpha():
        return "Consonant"
    else:
        return "Special"
