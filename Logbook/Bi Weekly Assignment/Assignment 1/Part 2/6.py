'''
6.Write a program to check whether a given year is a leap year or not.
'''

# Take year input from the user
a = int(input("Enter a year: "))

# Check if the year is a leap year
# Leap year condition: divisible by 4 and not by 100, or divisible by 400
if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
    print(a, "is a leap year.")
else:
    print(a, "is not a leap year.")
