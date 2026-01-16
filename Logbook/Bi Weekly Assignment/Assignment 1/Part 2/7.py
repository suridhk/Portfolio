'''
7.Write a program that takes a temperature in Celsius and prints whether it’s Cold (<10°C),
 Warm (10-825°C), or Hot (>25°C).
'''

# Take temperature input in Celsius
temp = float(input("Enter temperature in Celsius: "))

# Check if temperature is less than 10
if temp < 10:
    print("Temperature is Cold.")
# Check if temperature is between 10 and 25 (inclusive)
elif 10 <= temp <= 25:
    print("Temperature is Warm.")
# If temperature is greater than 25
else:
    print("Temperature is Hot")

