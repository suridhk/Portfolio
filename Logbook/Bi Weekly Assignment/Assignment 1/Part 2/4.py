'''
4.Write a program that prompts the user for an age, and prints whether the person is a child
(below 13), teenager (13–19), or adult (20 and above).
'''

# Take age input from the user
age = int(input("Enter your age: "))

# Check if age is less than 13
if age < 13:
    print("Child.")
# Check if age is between 13 and 19
elif 13 <= age <= 19:
    print("Teenager.")
# If age is 20 or above
else:
    print("Adult.")
