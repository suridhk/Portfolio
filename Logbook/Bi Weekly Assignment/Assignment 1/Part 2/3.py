'''
3. Write a program to convert Fahrenheit to Celsius and display the result rounded to two
decimal places.
'''

# Take temperature in Fahrenheit
F = float(input("Enter Fahrenheit: "))

# Convert Fahrenheit to Celsius
Celsius = (F - 32) * 5 / 9

# Round the result to 2 decimal places
c = round(Celsius, 2)

print("Celsius:", c)

