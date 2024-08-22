import random
from dataclasses import dataclass, field


def price_func():
    return float(random.randrange(20, 40))


@dataclass
class Book:
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0
    price: float = field(default_factory=price_func)


book1 = Book("Test1", "TestAuthor", 290)
book2 = Book("Test2", "TestAuthor", 240)

print(book1)
print(book2)
