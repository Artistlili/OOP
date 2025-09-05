class Book:
    def __init__(self, title, author):
        self.__title = title  # string
        self.__author = author  # string

    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author


class Library:
    def __init__(self):
        self.books = []  #array
    
    def add_book(self, book):
        self.books.append(book)

    def list_titles(self):
        for book in self.books:
            print(book.get_title())


book1 = Book("book a", "author a")
book2 = Book("book b", "author b")

library = Library()
library.add_book(book1)
library.add_book(book2)   

library.list_titles()

