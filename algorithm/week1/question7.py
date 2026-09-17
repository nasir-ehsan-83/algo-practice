# compute area and perimeter of rectangle
def rectangle_area_perimeter[T: (int, float)](length: T, width: T) -> tuple[T, T]:
    area: T = length * width;
    perimeter: T = 2 * (length + width);

    return area, perimeter;
