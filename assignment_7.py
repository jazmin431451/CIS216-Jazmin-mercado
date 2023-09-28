class Shape:
    """This class helps to support the color shapes."""

    def __init__(self, color):
        """Creates colors for shapes.

        Args:
            color (str): Color of the shape.

        """
        self.color = color

    @property
    def area(self):
        """Get the area of the shape.

        Returns:
            float: The area of the shape (0 by default for base class).
        """
        return 0

class Circle(Shape):
    """This class represents a colored circle."""

    def __init__(self, color, radius):
        """Creates a colored circle with a given radius.

        Args:
            color (str): Color of the circle.
            radius (float): Radius of the circle.
        """
        super().__init__(color)
        self.radius = radius

    @property
    def area(self):
        """Get the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    """This class represents a colored rectangle."""

    def __init__(self, color, width, height):
        """Creates a colored rectangle with given width and height.

        Args:
            color (str): Color of the rectangle.
            width (float): Width of the rectangle.
            height (float): Height of the rectangle.
        """
        super().__init__(color)
        self.width = width
        self.height = height

    @property
    def area(self):
        """Get the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height

# Main program to demonstrate polymorphism
def main():
    red_circle = Circle("Red", 5)
    blue_rectangle = Rectangle("Blue", 4, 6)

    # Polymorphism - referencing as the base class
    shapes = [red_circle, blue_rectangle]
    for shape in shapes:
        print("Color:", shape.color)
        print("Area:", shape.area)
        print()

    # Polymorphism - referencing as the subclass
    circle_as_shape = Shape("Green")
    print("Color:", circle_as_shape.color)
    print("Area (as Shape):", circle_as_shape.area)
    print()

if __name__ == "__main__":
    main()

