'''
1.Write a function that takes a string as input and returns:
The number of digits,
The number of alphabets
The number of special characters in that string.
'''

# Function to count alphabets, digits, and special characters in a string
def count_characters(a):
    letter = 0   # Initialize counter for alphabets
    digit = 0    # Initialize counter for digits
    special = 0  # Initialize counter for special characters

    # Loop through each character in the string
    for char in a:
        if char.isalpha():       # Check if character is a letter (A-Z or a-z)
            letter += 1
        elif char.isdigit():     # Check if character is a digit (0-9)
            digit += 1
        elif char != " ":        # Check if character is special (not a letter, not a digit, not a space)
            special += 1

    # Return counts of letters, digits, and special characters
    return letter, digit, special


# Take input string from the user
a = input("Enter a string: ")

# Call the function and store the results in l, d, s
l, d, s = count_characters(a)

# Print the results
print("Alphabets:", l)
print("Digits:", d)
print("Special characters:", s)



    