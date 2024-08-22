class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __eq__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Book must be of type 'Book'")
        return self.title == value.title and self.author == value.author and self.price == value.price

    def __ge__(self, value):  # Corrected method name
        if not isinstance(value, Book):
            raise ValueError("Book must be of type 'Book'")
        return self.price >= value.price

    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Book must be of type 'Book'")
        return self.price < value.price


b1 = Book('Python', 'Test', 5.0)
b2 = Book('C#', 'Test', 12.0)
b3 = Book('Angular', 'Test', 10.0)
print(b1 == b2)
print(b1 == b3)
print(b1 >= b3)
print(b1 < b3)

books = [b1, b2, b3]
books.sort()
print([book.title for book in books])