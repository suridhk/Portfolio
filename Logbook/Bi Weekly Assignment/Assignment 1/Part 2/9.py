'''
9.Write a program that asks the user to enter a number between 1 and 7, and displays the
 corresponding day of the week (1 for Sunday, 2 for Monday, etc.).
'''

# Ask the user to enter a number
n = int(input("Enter a number:"))

# Check if the number is outside the valid range (1 to 7)
if n < 1 or n > 7:
    # Display error message for invalid input
    print("Enter a number between 1 and 7 only!!!")

# If the number is valid, check each condition
elif n == 1:
    # If number is 1, display Sunday
    print("Sunday.")

elif n == 2:
    # If number is 2, display Monday
    print("Monday.")

elif n == 3:
    # If number is 3, display Tuesday
    print("Tuesday.")

elif n == 4:
    # If number is 4, display Wednesday
    print("Wednesday.")

elif n == 5:
    # If number is 5, display Thursday
    print("Thursday.")

elif n == 6:
    # If number is 6, display Friday
    print("Friday.")

elif n == 7:
    # If number is 7, display Saturday
    print("Saturday.")
