class Weather:
    def __init__(self, temperature, humidity, wind_speed):
        
        self.parameters = {
            'temperature': temperature,
            'humidity': humidity,
            'wind_speed': wind_speed
        }

    def __contains__(self, item):
       
        return item in self.parameters

    def display(self):
       
        print("Weather parameters:")
        for key, value in self.parameters.items():
            print(f"{key.capitalize()}: {value}")


weather = Weather(30, 65, 15)  

weather.display()


if 'temperature' in weather:
    print("\n'weather' contains 'temperature'.")
else:
    print("\n'weather' does not contain 'temperature'.")

if 'rainfall' in weather:
    print("'weather' contains 'rainfall'.")
else:
    print("'weather' does not contain 'rainfall'.")
