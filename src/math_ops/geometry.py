def rectangle_area_perimeter(length: float, width: float) -> tuple[float, float]:
    area: float = length * width
    perimeter: float = 2 * (length + width)
    return area, perimeter


def triangle_type(a: float, b: float, c: float) -> str:
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "Invalid"

    if a == b == c:
        return "Equilateral"

    if a == b or b == c or a == c:
        return "Isosceles"

    return "Scalene"
