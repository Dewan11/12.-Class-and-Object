import math

class Shape:
    def __init__(self):
        self.shape = ""
        self.value = 0

    def accept_data(self):
        self.shape = input("Enter shape (circle/square/triangle): ").lower()
        self.value = float(input("Enter value (radius or side length): "))

    def perimeter(self):
        if self.shape == "circle":
            return 2 * math.pi * self.value
        elif self.shape == "square":
            return 4 * self.value
        elif self.shape == "triangle":
            return 3 * self.value
        else:
            return "Invalid shape"

    def area(self):
        if self.shape == "circle":
            return math.pi * self.value**2
        elif self.shape == "square":
            return self.value**2
        elif self.shape == "triangle":
            return (math.sqrt(3) / 4) * self.value**2
        else:
            return "Invalid shape"

    def display(self):
        print(f"Perimeter/Circumference: {self.perimeter():.2f}")
        print(f"Area: {self.area():.2f}")


# Example usage
shape = Shape()
shape.accept_data()
shape.display()
