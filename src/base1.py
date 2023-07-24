def calculate_circle_area(radius):
    """
    calculate the area of a circle given its radius

    :param radius: the radius of the circle

    :return: the area of the circle
    """
    if not isinstance(radius, (int, float)):
        raise ValueError("Radius must be a number.")

    if radius < 0:
        raise ValueError("Radius cannot be negative")

    pi = 3.14159

    return pi * radius ** 2
