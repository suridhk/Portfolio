'''
11.Write a program to implement a class called employee with attributes such as empid,
name, address, contact_number, spouse name, number_of_child, salary. Instantiate this class
to input the values for multiple employees and write it in a file “employees.csv”. Allow the
user of your program to see the list of employees and their details as well. Try to use the
concept of try/except too in the program.
'''

# Employee class program with file handling

class Employee:
    def __init__(self, empid, name, address, contact, spouse, children, salary):
        self.empid = empid
        self.name = name
        self.address = address
        self.contact = contact
        self.spouse = spouse
        self.children = children
        self.salary = salary

    def to_csv(self):
        return f"{self.empid},{self.name},{self.address},{self.contact},{self.spouse},{self.children},{self.salary}\n"


try:
    file = open("employees.csv", "w")
    file.write("EmpID,Name,Address,Contact,Spouse,Children,Salary\n")

    n = int(input("How many employees do you want to add? "))

    for i in range(n):
        print("\nEnter details for Employee", i + 1)

        empid = input("Emp ID: ")
        name = input("Name: ")
        address = input("Address: ")
        contact = input("Contact Number: ")
        spouse = input("Spouse Name: ")
        children = input("Number of Children: ")
        salary = input("Salary: ")

        emp = Employee(empid, name, address, contact, spouse, children, salary)
        file.write(emp.to_csv())

    file.close()
    print("\nEmployee data saved to employees.csv")

except:
    print("Error while writing to file!")

# Display employee details
try:
    file = open("employees.csv", "r")
    print("\nEmployee List:")
    for line in file:
        print(line.strip())
    file.close()

except:
    print("Error while reading file!")
