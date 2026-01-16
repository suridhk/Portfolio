'''
6.Write a program that reads a text file and writes all unique words (no duplicates) into a new
file, sorted alphabetically.
'''

# Program to write unique words from a file into another file (sorted)

input_file = input("Enter the input filename: ")
output_file = input("Enter the output filename: ")

try:
    file = open(input_file, "r")
    text = file.read()
    file.close()

    words = text.split()      # Split text into words
    unique_words = set(words) # Remove duplicates
    sorted_words = sorted(unique_words)  # Sort alphabetically

    out = open(output_file, "w")
    for word in sorted_words:
        out.write(word + "\n")
    out.close()

    print("Unique words written to", output_file)

except:
    print("File not found!")
