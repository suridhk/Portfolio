'''
7.Write a program that reads a file and counts how many lines begin with a vowel (A, E, I, O,U).
'''

# Program to count lines that start with a vowel

filename = input("Enter the filename: ")

try:
    file = open(filename, "r")
    count = 0

    for line in file:
        line = line.strip()   # Remove leading spaces and newline
        if line != "":
            if line[0] in "AEIOUaeiou":
                count += 1

    file.close()

    print("Number of lines starting with a vowel:", count)

except:
    print("File not found!")
