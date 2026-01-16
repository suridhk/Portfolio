import random
import sys

# ==========================================
# TASK 2: PASSWORD SECURITY CHECK
# ==========================================

# Ask the user to enter their password
password = input("Enter your password: ")

# Check if password length is at least 9 characters
if len(password) < 9:
    print("Password too short !! Enter atleast 9 characters ")
    sys.exit()   # Stop the program

# Ask the user for 3 random letters from the password
for check in range(3):

    # Choose a random position (1 to length of password)
    position = random.randint(1, len(password))

    # Ask the user for the letter at that position
    user_letter = input(f"Enter letter at position {position}: ")

    # Check if the letter is correct
    if user_letter == password[position - 1]:
        print("Correct")
    else:
        print("Security check failed.")
        sys.exit()   # Stop immediately if wrong

# If all checks are correct
print("Security check passed.")
