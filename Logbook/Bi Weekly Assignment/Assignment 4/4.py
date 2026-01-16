'''
4.Create a Python module named math_utils.py containing functions for:
factorial
square
cube
Then, in another file (main.py), import that module and use its functions.
'''

# math_utils.py

# Function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Function to calculate square
def square(n):
    return n * n

# Function to calculate cube
def cube(n):
    return n * n * n
