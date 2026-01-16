'''
8.Write a program that reads a text file and reverses the contents of each line, then writes the
reversed lines into a new file called reversed.txt.
'''

# Program to reverse each line of a file and save to reversed.txt

filename = input("Enter the input filename: ")

try:
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    out = open("reversed.txt", "w")

    for line in lines:
        reversed_line = line[::-1]   # Reverse the line
        out.write(reversed_line)

    out.close()

    print("Reversed lines written to reversed.txt")

except:
    print("File not found!")
