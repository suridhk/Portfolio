'''
1. Write a program to take a number input from the user and display whether the number is
positive, negative, or zero.
'''

# Take an integer input from the user
n = int(input("Enter a number: "))

# Check if the number is positive
if n > 0:
    print(n, "is a positive number.")
# Check if the number is zero
elif n == 0:
    print(n, "is zero.")
# If the number is negative
else:
    print(n, "is a negative number.")

