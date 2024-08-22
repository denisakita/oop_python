""" Create a basic class"""

from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    def bookinfo(self):
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}"


""" Create instances of the class"""

book1 = Book("Test1", "TestAuthor", 290, 300)
book2 = Book("Test2", "TestAuthor", 240, 500)

""" Print the class and property"""
print(book1)
print(book2)
print("---------------------------")

print(book1 == book2)
print("---------------------------")
book1.title = "TestTitle"
print(book1.bookinfo())
