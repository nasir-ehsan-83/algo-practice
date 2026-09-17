def grade(marks: float) -> str:
    if marks >= 90: return 'A';
    elif marks >= 80: return 'B';
    elif marks >= 70: return 'C';
    elif marks >= 60: return 'D';
    else: return 'F';
