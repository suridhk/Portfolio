'''
8.Write a program using lambda functions and map() to square each number in a list
[1, 2, 3, 4, 5].
Then use filter() to return only the squared values greater than 10.
'''

# Original list
numbers = [1, 2, 3, 4, 5]

# Use lambda and map to square each number
squared = list(map(lambda x: x**2, numbers))
print("Squared values:", squared)

# Use lambda and filter to get values greater than 10
filtered = list(filter(lambda x: x > 10, squared))
print("Squared values greater than 10:", filtered)
