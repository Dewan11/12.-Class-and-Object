class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def display(self):
        if self.imag >= 0:
            print(f"{self.real} + {self.imag}i")
        else:
            print(f"{self.real} - {-self.imag}i")

    def add(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def subtract(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def multiply(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def divide(self, other):
        denom = other.real**2 + other.imag**2
        if denom == 0:
            print("Cannot divide by zero!")
            return None
        real = (self.real * other.real + self.imag * other.imag) / denom
        imag = (self.imag * other.real - self.real * other.imag) / denom
        return Complex(real, imag)


# Short example usage
a = Complex(4, 5)
b = Complex(2, -3)

a.add(b).display()
a.subtract(b).display()
a.multiply(b).display()
result = a.divide(b)
if result:
    result.display()
