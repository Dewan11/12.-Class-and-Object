class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def display(self):
       
        print(f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}")

    def add(self, other):
       
        total_seconds = self.to_seconds() + other.to_seconds()
        return Time.from_seconds(total_seconds)

    def subtract(self, other):
       
        total_seconds = self.to_seconds() - other.to_seconds()
        return Time.from_seconds(total_seconds)

    def to_seconds(self):
        
        return self.hours * 3600 + self.minutes * 60 + self.seconds

 
    def from_seconds(total_seconds):
        
        hours = total_seconds // 3600
        total_seconds %= 3600
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return Time(hours, minutes, seconds)



time1 = Time(2, 45, 30)  
time2 = Time(1, 15, 50)  

print("Time 1:")
time1.display()

print("Time 2:")
time2.display()


result_add = time1.add(time2)
print("\nTime 1 + Time 2:")
result_add.display()


result_sub = time1.subtract(time2)
print("\nTime 1 - Time 2:")
result_sub.display()
