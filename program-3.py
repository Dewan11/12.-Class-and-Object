import math

class Cylinder:
    def __init__(self):
        self.radius = 0
        self.height = 0

    def accept_data(self):
        self.radius = float(input("Enter radius: "))
        self.height = float(input("Enter height: "))

    def surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def volume(self):
        return math.pi * self.radius**2 * self.height

    def display(self):
        print(f"Surface Area: {self.surface_area():.2f}")
        print(f"Volume: {self.volume():.2f}")


# Example usage
solid = Cylinder()
solid.accept_data()
solid.display()
