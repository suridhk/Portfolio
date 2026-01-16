'''
9.Write a one-line list comprehension to produce a list of all numbers between 1 and
100 that are divisible by both 3 and 5.
'''

# List of numbers between 1 and 100 divisible by both 3 and 5
numbers = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]

print(numbers)
