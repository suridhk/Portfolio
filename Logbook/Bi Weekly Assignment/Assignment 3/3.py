'''
3. Write a program that searches for a specific word in a text file and prints the line numbers
where that word occurs.
'''

# Program to search a word in a file and print line numbers

filename = input("Enter the filename: ")
word = input("Enter the word to search: ")

try:
    file = open(filename, "r")
    line_number = 1

    for line in file:
        if word in line:
            print("Word found at line:", line_number)
        line_number += 1

    file.close()

except:
    print("File not found!")
