'''
2.Write a function named safe_int_input() that continuously prompts the user for an
integer value until a valid integer is entered.
If the user enters something invalid, catch the exception and prompt again.
'''

# Function to safely get an integer input from the user
def safe_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value  # Return the valid integer
        except ValueError:
            print("Invalid input! Please enter an integer.")

# Example usage
num = safe_int_input("Enter an integer: ")
print("You entered:", num)
