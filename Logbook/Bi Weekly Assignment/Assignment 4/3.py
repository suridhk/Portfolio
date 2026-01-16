'''
3.Write a program to open a file specified by the user.
If the file doesn’t exist, handle the FileNotFoundError gracefully and display an
appropriate message.
'''

# Program to open a file and handle FileNotFoundError

filename = input("Enter the filename: ")

try:
    file = open(filename, "r")  # Try to open the file in read mode
    content = file.read()
    file.close()
    print("File opened successfully!")
    print("Content of the file:\n")
    print(content)

except FileNotFoundError:
    print("Error: The file does not exist. Please check the filename and try again.")
