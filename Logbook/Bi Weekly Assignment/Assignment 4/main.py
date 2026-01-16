# main.py

# Import the converter module
import converter

# Example usage
km = float(input("Enter distance in kilometers: "))
c = float(input("Enter temperature in Celsius: "))

miles = converter.km_to_miles(km)
fahrenheit = converter.celsius_to_fahrenheit(c)

print(f"{km} km is equal to {miles} miles.")
print(f"{c}°C is equal to {fahrenheit}°F.")
