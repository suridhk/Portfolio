'''
4.Write a function that accepts a list of numbers and returns a new list containing only the
even numbers, sorted in ascending order.
'''

def get_even_numbers(numbers):
    # Create an empty list to store even numbers
    even_numbers = []

    # Loop through each number in the list
    for n in numbers:
        # Check if the number is even
        if n % 2 == 0:
            # Add the even number to the list
            even_numbers.append(n)

    # Sort the list of even numbers in ascending order
    even_numbers.sort()

    # Return the sorted list of even numbers
    return even_numbers


# Example list of numbers
nums = [5, 2, 8, 1, 4, 7]

# Call the function and store the result
result = get_even_numbers(nums)

# Print the final result
print(result)
