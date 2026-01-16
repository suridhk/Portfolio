'''
2.Write a function to check whether a given number is a perfect number or not.
(A perfect number is equal to the sum of its proper divisors, e.g., 6 = 1 + 2 + 3)
'''

# Function to check if a number is perfect
def perfect_number(n):
    sum = 0   # Initialize sum to store sum of proper divisors

    # Loop through all numbers from 1 to n-1 to find proper divisors
    for i in range(1, n):
        if n % i == 0:        # Check if i divides n exactly
            sum = sum + i     # Add divisor to sum

    # Check if sum of divisors equals the original number
    if sum == n:
        return True           # n is a perfect number
    else:
        return False          # n is not a perfect number


# Take input from the user
n = int(input("Enter a number:"))

# Call the function and print the result
if perfect_number(n):
    print("Is a perfect number.")
else:
    print("Not a perfect number. Enter a perfect number!!")


