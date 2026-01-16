'''
13.Write a Python program to find those numbers which are divisible by 7 and multiple of 5,
between 1500 and 2000 (both included).
'''

for n in range(1500, 2001):
    # Check if the number is divisible by 7 and also a multiple of 5
    if n % 7 == 0 and n % 5 == 0:
        # Print the number if both conditions are true
        print(n)
