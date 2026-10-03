def is_leap_year(year: int) -> bool:
    if year % 4 != 0:
        return False

    elif year % 100 != 0:
        return True

    return year % 400 == 0


def month_info(month: int) -> tuple[str, int]:
    months: dict[int, tuple[str, int]] = {
        1: ("January", 31),
        2: ("February", 28),
        3: ("March", 31),
        4: ("April", 30),
        5: ("May", 31),
        6: ("June", 30),
        7: ("July", 31),
        8: ("August", 31),
        9: ("September", 30),
        10: ("October", 31),
        11: ("November", 30),
        12: ("December", 31),
    }
    return months.get(month, ("Invalid", 0))


def seconds_to_hms(seconds: int) -> tuple[int, int, int]:
    h: int = seconds // 3600
    seconds %= 3600
    m: int = seconds // 60
    s: int = seconds % 60
    return h, m, s
