'''
14.Write a Python program that accepts a string and calculates the number of digits and
letters.
'''

# Accept a string input from the user
text = input("Enter a string: ")

# Initialize counters for letters and digits
letters = 0
digits = 0

# Loop through each character in the string
for char in text:
    # Check if the character is a letter
    if char.isalpha():
        letters += 1
    # Check if the character is a digit
    elif char.isdigit():
        digits += 1

# Display the counts
print("Letters:", letters)
print("Digits:", digits)


