'''
10.Write a program that takes a distance in kilometers and converts it to miles, displaying the
   result with exactly three decimal places.
'''

# Take distance in kilometers from the user
k = float(input("Enter distance in kilometers:"))

# Convert kilometers to miles using conversion factor
m = k * 0.621

# Round the converted value to 3 decimal places
a = round(m, 3)

# Display the result with exactly three decimal places
print(k, "km =", format(a, ".3f"), "miles")

