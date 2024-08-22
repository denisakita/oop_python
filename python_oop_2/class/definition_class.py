""" Create a basic class"""


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


""" Create instances of the class"""

book1 = Book("Test1", "TestAuthor", 2024)
book2 = Book("Test2", "TestAuthor", 2025)

""" Print the class and property"""
print(book1)
print(book2)
