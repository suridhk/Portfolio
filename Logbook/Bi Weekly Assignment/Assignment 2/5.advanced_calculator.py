'''
5.Create a program named advanced_calculator with functions to perform the following:
A. Square root
B. Absolute value
C. Floor division
D. Percentage (first number as a percent of the second)
E. Average of two numbers
Each should accept the required parameters and return the computed result.
'''

import math

# Function to calculate square root
def square_root(num):
    return math.sqrt(num)

# Function to calculate absolute value
def absolute_value(num):
    return abs(num)

# Function for floor division
def floor_division(a, b):
    return a // b

# Function for percentage
def percentage(a, b):
    return (a / b) * 100

# Function for average of two numbers
def average(a, b):
    return (a + b) / 2


# Main program
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Square root of first number:", square_root(a))
print("Absolute value of first number:", absolute_value(a))
print("Floor division of a // b:", floor_division(a, b))
print("Percentage of first number w.r.t second:", percentage(a, b))
print("Average of the two numbers:", average(a, b))
