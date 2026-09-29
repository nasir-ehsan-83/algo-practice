def is_leap_year(year: int) -> bool:
    if year % 4 != 0:
        return False

    elif year % 100 != 0:
        return True

    return year % 400 == 0
