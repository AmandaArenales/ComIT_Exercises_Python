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
    copies_book = 0
    lended_copies = 0

    def __init__(self):
        pass

    def __init__(self, title, author, copies_book, lended_copies):
       self.title = title
       self.author = author
       self.copies_book = copies_book
       self.lended_copies = lended_copies
   
    def get_title(self):
        return self.title
    
    def get_lended_copies(self):
        return self.lended_copies
    
    def available_copies(self):
        return self.copies_book - self.lended_copies
    
    def borrow_book(self):
        if self.available_copies() > 0:
            self.lended_copies +=1
            return True
        else:
            return False
        
    def return_book(self):
        if self.lended_copies > 0:
            self.lended_copies -= 1
            return True
        else:
            return False

    def __str__(self):
        return ("\nBook: " + self.title + 
                "\nAuthor: "+ self.author + 
                "\nTotal of book's copies: " + str(self.copies_book) + 
                "\nLended copies: " + str(self.lended_copies)) 

class LibrarySystem:
    books = []

    def insert_book(self, title, author, copies_book, lended_copies):
        book = Book(title, author, copies_book, lended_copies)
        self.books.append(book)
  
    def borrow_book(self):
        title = input("\nPlease, insert the book's title that you want to borrow: ")
        for b in self.books:
            if b.get_title() == title: 
                if b.borrow_book():
                    print(f"You can borrow the book {title}.")
                else: 
                    print("There are no copies avalible at this moment. You will be at the wait list.")
    
    def return_book(self):
        title = input("\nPlease, insert the book's title that you want to return: ")
        for b in self.books:
            if (title == b.get_title()) and (b.get_lended_copies() > 0) :
                b.return_book()
                print(f"The {title} was returned successfuly.")
            return False
    
    def list_books(self):
        for b in self.books:
            print(b)
        
lib = LibrarySystem()
lib.insert_book("Brave, Not Perfect", "Reshma Saujani", 25, 6)
lib.insert_book("The light We Carry", "Michelle Obama", 50, 25)
lib.insert_book("I Am Malala", " Malala Yousafzai", 40, 16)
lib.insert_book("Becoming", "Michelle Obama", 35, 10)
lib.insert_book("A Promised Land", "Barack Obama", 30, 15)

lib.borrow_book()
lib.borrow_book()

lib.return_book()
lib.return_book()

lib.list_books()
