# Python oop -- some dunder methods
# Python OOP - Library Management System
class Book:

    def __init__(self, title, author, price, copies):
        self.title = title
        self.author = author
        self.price = price
        self.copies = copies

    def __str__(self):
        return f"Title : {self.title}\nAuthor : {self.author}\n Price : {self.price}\n Copies : {self.copies}"

    def __repr__(self):
        return f"Book(title={self.title}, author={self.author}, price={self.price}, copies={self.copies})"


book1 = Book("Python Crash Course", "Eric Matthes", 899, 5)

print(book1.title)
print(book1.author)
print(book1.price)
print(book1.copies)

print(str(book1))
print(repr(book1))
