'''
6.Write a program that defines a class Rectangle with attributes length and width, and
methods to compute the area and perimeter.
Create two objects of the class and display their results.
'''

# Rectangle class program

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method to calculate area
    def area(self):
        return self.length * self.width

    # Method to calculate perimeter
    def perimeter(self):
        return 2 * (self.length + self.width)


# Create two objects of Rectangle
rect1 = Rectangle(5, 3)
rect2 = Rectangle(10, 7)

# Display results for rect1
print("Rectangle 1:")
print("Length:", rect1.length)
print("Width:", rect1.width)
print("Area:", rect1.area())
print("Perimeter:", rect1.perimeter())

print("\nRectangle 2:")
print("Length:", rect2.length)
print("Width:", rect2.width)
print("Area:", rect2.area())
print("Perimeter:", rect2.perimeter())
