class Rectangle:
    def __init__(self, width, height):
        # Initialize a Rectangle object with width and height attributes.
        self.width = width
        self.height = height
    
    def set_width(self, width):
        # Set the width attribute of the Rectangle.
        self.width = width
    
    def set_height(self, height):
        # Set the height attribute of the Rectangle.
        self.height = height
    
    def get_area(self):
        # Calculate and return the area of the Rectangle.
        return self.width * self.height
    
    def get_perimeter(self):
        # Calculate and return the perimeter of the Rectangle.
        return 2 * (self.width + self.height)
    
    def get_diagonal(self):
        # Calculate and return the diagonal length of the Rectangle.
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self):
        # Generate a string representation of the Rectangle using '*'.
        # If the dimensions are too big, return "Too big for picture."
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return '\n'.join(['*' * self.width for _ in range(self.height)]) + '\n'
    
    def get_amount_inside(self, shape):
        # Calculate how many times the given shape can fit inside this Rectangle.
        width_fit = self.width // shape.width
        height_fit = self.height // shape.height
        return width_fit * height_fit
    
    def __str__(self):
        # Return a string representation of the Rectangle object.
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        # Initialize a Square object with a given side length.
        # Both width and height attributes are set to the side length.
        super().__init__(side, side)
    
    def set_side(self, side):
        # Set the side length of the Square by updating width and height.
        self.width = side
        self.height = side
    
    def set_width(self, width):
        # Override set_width method to ensure Square maintains its properties.
        self.set_side(width)
    
    def set_height(self, height):
        # Override set_height method to ensure Square maintains its properties.
        self.set_side(height)
    
    def __str__(self):
        # Return a string representation of the Square object.
        return f"Square(side={self.width})"
