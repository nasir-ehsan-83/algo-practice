def rectangle_area_perimeter[T: (int, float)](length: T, width: T) -> tuple[T, T]:
    area: T = length * width
    perimeter: T = 2 * (length + width)
    return area, perimeter


def triangle_type[T: (int, float)](a: T, b: T, c: T) -> str:
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "Invalid"

    if a == b == c:
        return "Equilateral"

    if a == b or b == c or a == c:
        return "Isosceles"

    return "Scalene"
