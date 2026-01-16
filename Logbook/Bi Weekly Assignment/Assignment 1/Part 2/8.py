'''
8 .Write a program to take a character input and display whether it is a vowel or consonant.
'''

# Take character input and convert to lowercase
n = input("Enter a character: ").lower()  # .lower() makes the check case-insensitive

# Check if the character is a vowel
if n in 'aeiou':
    print("Vowel")
else:
    print("Consonant")

