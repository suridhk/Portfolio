'''
1.Write a program that asks the user to enter two numbers and performs division.
Use try…except to handle:
Division by zero
Invalid input (non-numeric values)
Print appropriate error messages in each case.
'''

# Program to perform division with error handling

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")

except ValueError:
    print("Error: Invalid input! Please enter numeric values.")
