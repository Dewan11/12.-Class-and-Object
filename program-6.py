class Date:
    def __init__(self, day, month, year):
       
        self.day = day
        self.month = month
        self.year = year

    def __eq__(self, other):
       
        return (self.day == other.day) and (self.month == other.month) and (self.year == other.year)

    def display(self):
        
        print(f"{self.day:02}-{self.month:02}-{self.year}")


date1 = Date(15, 8, 2025)
date2 = Date(15, 8, 2025)
date3 = Date(10, 5, 2023)

print("Date 1:")
date1.display()

print("Date 2:")
date2.display()

print("Date 3:")
date3.display()


if date1 == date2:
    print("\nDate 1 and Date 2 are the same.")
else:
    print("\nDate 1 and Date 2 are different.")

if date1 == date3:
    print("Date 1 and Date 3 are the same.")
else:
    print("Date 1 and Date 3 are different.")
