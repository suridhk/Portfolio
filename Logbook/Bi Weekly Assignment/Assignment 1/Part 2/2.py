'''
2.Write a program that asks for two integers and displays the remainder and quotient after
dividing the first by the second.
'''

# Take two integer inputs
a = int(input("Enter an integer: "))
b = int(input("Enter another integer: "))

# Check if the second number is zero to avoid division error
if b == 0:
    print("Please enter a non-zero value for the second number.")
else:
    # Calculate remainder using modulus operator
    remainder = a % b

    # Calculate quotient using floor division
    quotient = a // b

    print("The remainder is:", remainder)
    print("The quotient is:", quotient)
