# Reverse a string
def reverse_string(s: str) -> str:
    reversed_str: str = "";

    for i in range(len(s)-1, -1, -1):
        reversed_str += s[i];
    
    return reversed_str;
