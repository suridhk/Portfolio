'''
1.Write a program that reads a text file and prints the number of vowels, consonants, digits,
and special characters it contains.
'''

# Open the file in read mode
filename = input("Enter the filename (with extension): ")
try:
    with open(filename, 'r') as file:
        text = file.read()

    # Initialize counters
    vowels = 0
    consonants = 0
    digits = 0
    special_chars = 0

    # Define vowels
    vowel_letters = "aeiouAEIOU"

    # Loop through each character in the text
    for char in text:
        if char.isalpha():  # Check if it is a letter
            if char in vowel_letters:
                vowels += 1
            else:
                consonants += 1
        elif char.isdigit():  # Check if it is a digit
            digits += 1
        elif not char.isspace():  # Special characters (ignore spaces)
            special_chars += 1

    # Print the results
    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("Digits:", digits)
    print("Special Characters:", special_chars)

except FileNotFoundError:
    print("File not found. Please check the filename and try again.")

