'''
2. Write a program to merge the contents of two text files into a third file. The third file
should contain the combined contents of both, separated by a line "----- End of File 1 -----".
'''

# Program to merge two files into a third file

# Get the filenames from the user
file1 = input("Enter the first filename: ")
file2 = input("Enter the second filename: ")
merged_file = input("Enter the filename for the merged file: ")

try:
    # Open first file and read its content
    with open(file1, "r") as f1:
        content1 = f1.read()

    # Open second file and read its content
    with open(file2, "r") as f2:
        content2 = f2.read()

    # Open the merged file in write mode
    with open(merged_file, "w") as f3:
        f3.write(content1)  # Write content of first file
        f3.write("\n----- End of File 1 -----\n")  # Separator line
        f3.write(content2)  # Write content of second file

    print("Files merged successfully into", merged_file)

except FileNotFoundError:
    print("One of the files was not found. Please check the filenames.")
