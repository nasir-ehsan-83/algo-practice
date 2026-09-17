def seconds_to_hms(seconds: int) -> tuple[int, int, int]:
    h: int = seconds // 3600;
    seconds %= 3600;
    m: int = seconds // 60;
    s: int = seconds % 60;

    return h, m, s;
