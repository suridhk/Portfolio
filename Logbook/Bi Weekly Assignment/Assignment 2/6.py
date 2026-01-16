'''
6.Write a program that prompts the user for 10 integer inputs and stores only unique values in
a list. Display the sorted list of unique numbers at the end.
'''

unique_numbers = []

for i in range(10):
    n = int(input("Enter Ten integer: "))

    # Add only if the number is not already in the list
    if n not in unique_numbers:
        unique_numbers.append(n)

# Sort the list after all inputs
unique_numbers.sort()

# Display the sorted list of unique numbers
print("Sorted unique numbers:", unique_numbers)


