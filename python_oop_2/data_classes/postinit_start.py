from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    def __post_init__(self):
        self.description = self.title + ' - ' + self.author


book1 = Book("Test1", "TestAuthor", 290, 300)
book2 = Book("Test2", "TestAuthor", 240, 500)

print(book1.description)
print(book2.description)
