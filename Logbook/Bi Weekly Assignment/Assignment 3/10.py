'''
10. Create a class Student with the attributes such as id, name, address, admission year, level,
section. Instantiate the object of class to take input for all the attributes and display the output.
'''

# Student class program

class Student:
    def __init__(self, id, name, address, admission_year, level, section):
        self.id = id
        self.name = name
        self.address = address
        self.admission_year = admission_year
        self.level = level
        self.section = section

    def display(self):
        print("\nStudent Details")
        print("ID:", self.id)
        print("Name:", self.name)
        print("Address:", self.address)
        print("Admission Year:", self.admission_year)
        print("Level:", self.level)
        print("Section:", self.section)


# Taking input from the user
id = input("Enter ID: ")
name = input("Enter Name: ")
address = input("Enter Address: ")
admission_year = input("Enter Admission Year: ")
level = input("Enter Level: ")
section = input("Enter Section: ")

# Creating object of Student class
student1 = Student(id, name, address, admission_year, level, section)

# Displaying student details
student1.display()
