'''
12.Write a program to implement a basic library book management with the functionalities
such as issue the book, return the book and search the book. Use the concept of OOP to create
the necessary classes on your own and implement the concept of other OOP features. For the
storage of book details, use the file handling along with the exception handling.
'''

# Basic Library Book Management System

class Book:
    def __init__(self, book_id, title, author, status="Available"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = status

    def to_file(self):
        return f"{self.book_id},{self.title},{self.author},{self.status}\n"


class Library:
    def add_book(self):
        try:
            file = open("library.txt", "a")
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")

            book = Book(book_id, title, author)
            file.write(book.to_file())
            file.close()

            print("Book added successfully!")

        except:
            print("Error while adding book!")

    def search_book(self):
        try:
            book_id = input("Enter Book ID to search: ")
            file = open("library.txt", "r")

            found = False
            for line in file:
                data = line.strip().split(",")
                if data[0] == book_id:
                    print("Book Found:")
                    print("ID:", data[0])
                    print("Title:", data[1])
                    print("Author:", data[2])
                    print("Status:", data[3])
                    found = True

            file.close()
            if not found:
                print("Book not found!")

        except:
            print("Error while searching book!")

    def issue_book(self):
        try:
            book_id = input("Enter Book ID to issue: ")
            file = open("library.txt", "r")
            lines = file.readlines()
            file.close()

            file = open("library.txt", "w")
            issued = False

            for line in lines:
                data = line.strip().split(",")
                if data[0] == book_id and data[3] == "Available":
                    data[3] = "Issued"
                    issued = True
                file.write(",".join(data) + "\n")

            file.close()

            if issued:
                print("Book issued successfully!")
            else:
                print("Book not available or not found!")

        except:
            print("Error while issuing book!")

    def return_book(self):
        try:
            book_id = input("Enter Book ID to return: ")
            file = open("library.txt", "r")
            lines = file.readlines()
            file.close()

            file = open("library.txt", "w")
            returned = False

            for line in lines:
                data = line.strip().split(",")
                if data[0] == book_id and data[3] == "Issued":
                    data[3] = "Available"
                    returned = True
                file.write(",".join(data) + "\n")

            file.close()

            if returned:
                print("Book returned successfully!")
            else:
                print("Book not found or not issued!")

        except:
            print("Error while returning book!")


# Main Program
library = Library()

while True:
    print("\nLibrary Menu")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.search_book()
    elif choice == "3":
        library.issue_book()
    elif choice == "4":
        library.return_book()
    elif choice == "5":
        print("Thank you! Exiting program.")
        break
    else:
        print("Invalid choice!")
