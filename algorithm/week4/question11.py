def is_rotation[T](s1: list[T], s2: list[T]) -> bool:
    if len(s1) != len(s2):
        return False;

    return s2 in (s1 + s1);
