'''
5.Write a program that accepts three numbers from the user and prints the largest among
  them.
'''

# Take three integer inputs from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Check if 'a' is the greatest
if a > b and a > c:
    print(a, "is the greatest.")
# Check if 'b' is the greatest
elif b > a and b > c:
    print(b, "is the greatest.")
# If neither 'a' nor 'b' is the greatest, 'c' must be
else:
    print(c, "is the greatest.")

