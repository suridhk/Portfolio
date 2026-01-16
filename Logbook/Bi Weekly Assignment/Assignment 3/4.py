'''
4. Write a program that reads a CSV file containing student names and marks, and prints the
data in a well-formatted table, showing name, mark, and grade (A/B/C based on ranges).
'''

# Program to read a CSV file and display name, marks and grade

filename = input("Enter the CSV filename: ")

try:
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    print("\nName\tMarks\tGrade")
    print("------------------------")

    for line in lines[1:]:   # Skip header line
        name, marks = line.strip().split(",")
        marks = int(marks)

        if marks >= 80:
            grade = "A"
        elif marks >= 60:
            grade = "B"
        else:
            grade = "C"

        print(name, "\t", marks, "\t", grade)

except:
    print("File not found!")
