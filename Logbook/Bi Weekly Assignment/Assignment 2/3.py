'''
3.Write a function to determine whether a given number is a palindrome number or not.
(Example: 121 → Palindrome, 123 → Not a palindrome)
'''

# Function to check if a number is a palindrome
def pal(n):
    temp = n        # Store the original number in 'temp' because 'n' will be modified
    rev = 0         # Initialize 'rev' to build the reversed number

    # Loop to reverse the number
    while n > 0:
        a = n % 10          # Get the last digit of 'n'
        rev = (rev * 10) + a # Add the digit to 'rev', shifting previous digits left
        n = n // 10          # Remove the last digit from 'n'

    # Check if the reversed number is equal to the original number
    if rev == temp:
        return True         # Number is a palindrome
    else:
        return False        # Number is not a palindrome

# Input from the user
n = int(input("Enter a number:"))

# Check the number using the 'pal' function
if pal(n):
    print("Palindrome.")       # Output if the number is a palindrome
else:
    print("Not a Palindrome.") # Output if the number is not a palindrome
