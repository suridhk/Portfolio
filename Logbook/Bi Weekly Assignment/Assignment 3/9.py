'''
9.Write a program that reads a CSV file containing employee data (name, department, salary)
and prints the average salary per department.
'''

# Program to calculate average salary per department

filename = input("Enter the CSV filename: ")

try:
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    total_salary = {}
    count = {}

    for line in lines[1:]:   # Skip header
        name, dept, salary = line.strip().split(",")
        salary = int(salary)

        if dept in total_salary:
            total_salary[dept] += salary
            count[dept] += 1
        else:
            total_salary[dept] = salary
            count[dept] = 1

    print("\nDepartment\tAverage Salary")
    print("-----------------------------")

    for dept in total_salary:
        average = total_salary[dept] / count[dept]
        print(dept, "\t\t", average)

except:
    print("File not found!")
