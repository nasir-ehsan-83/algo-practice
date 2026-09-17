def seconds_to_hms(seconds: float) -> tuple[float, float, float]:
    h = seconds // 3600;
    seconds %= 3600;
    m = seconds // 60;
    s = seconds % 60;

    return h, m, s;