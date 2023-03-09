"""Create a class called Book that stores the information for each of the books in a library. The class 
should keep the title of the book, author, number of copies of the book and number of lend copies. 
The class will contain the following methods: Default constructor. Constructor with parameters. 
Setters / getters. Method Loan that increases the corresponding attribute each time a loan is 
made from the book. No books may be borrowed if no copies are available to lend. Returns true if the 
operation was successful and false otherwise.  Returns method that decrements the corresponding attribute
when a book is returned. No books can be returned that have not been lend. Returns true if the operation 
was successful and false otherwise. ToString method to display data from books. This method is inherited 
from Object and we must modify it (override) to adapt it to the Book class. 
Write a program to test the operation of the Book class."""

class Book:
    title = ""
    author = ""

    def __init__(self, title, author):
       self.title = title
       self.author = author
  
    def copies_book(self, copies_book):
        self.copies_book = copies_book
    
    def lend_copies(self, lend_copies):
        self.lend_copies = lend_copies

class LibrarySystem:
    books = []
    def __init__(self):
        book = Book()
        self.books.append(book)

    def avalible_copies(self, avalible_copies):
        self.avalible_copies = self.set_copies_book - self.set_lend_copies
     
    def borrow_book(self):
        if available_copies > 0:
            available_copies -=1
        else:
            print("There are no copies avalible at this moment. You will be at the wait list.")

    def get_title(self):
        return title
    
    def return_book(self):
        for b in books:
            if title == b.get_title():
                available_copies += 1
                print(f"The {title} was returned successfuly.")
            return False
 

book = Book("The light we carry", "Michele")
print(book)
