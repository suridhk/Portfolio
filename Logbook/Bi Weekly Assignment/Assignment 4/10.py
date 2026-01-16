'''
10.Write a program that reads a list of numbers from the user and finds the second
largest number.
Handle the following exceptions:
User enters fewer than two numbers
User enters non-numeric values
'''

try:
    # Read numbers from user
    user_input = input("Enter numbers separated by spaces: ")
    numbers = [float(x) for x in user_input.split()]  # Convert to float

    # Check if there are at least two numbers
    if len(numbers) < 2:
        raise ValueError("You must enter at least two numbers!")

    # Remove duplicates and sort descending
    unique_numbers = list(set(numbers))
    unique_numbers.sort(reverse=True)

    # Find second largest
    second_largest = unique_numbers[1]
    print("The second largest number is:", second_largest)

except ValueError as e:
    print("Error:", e)
