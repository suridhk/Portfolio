'''
12.Write a program to find the simple interest when the value of principle, rate of interest and
time period is provided by the user.
'''

# Take the principal amount from the user
p = float(input("Enter Principle: "))

# Take the rate of interest from the user
r = float(input("Enter Rate: "))

# Take the time period from the user
t = float(input("Enter Time Period: "))

# Calculate simple interest using the formula SI = (P × R × T) / 100
si = p * r * t / 100

# Display the calculated simple interest
print(f"The Simple Interest is: {si}")
