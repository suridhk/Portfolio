'''
11. Write a program to find the Euclidean distance between two coordinates. Take both the
coordinates from the user as input.
'''

import math
 
# Getting the first coordinate (Point 1)
x1 = float(input("Enter x-coordinate for Point 1: "))
y1 = float(input("Enter y-coordinate for Point 1: "))

# Getting the second coordinate (Point 2)

x2 = float(input("Enter x-coordinate for Point 2: "))
y2 = float(input("Enter y-coordinate for Point 2: "))

a = (x2-x1) **2 + (y2-y1)**2
n = math.sqrt(a)

print(f" The Euclidean distance between two coordinates is: {n}")