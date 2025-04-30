class String:
    def __init__(self, value=""):
        self.value = value

    def __iadd__(self, other):
        self.value += str(other)
        return self

    def toLower(self):
        self.value = self.value.lower()

    def toUpper(self):
        self.value = self.value.upper()

    def display(self):
        print(self.value)


str1 = String("Hello")
str2 = String(" World!")

str1 += str2
str1.display() 

str1.toLower()
str1.display()  

str1.toUpper()
str1.display() 
