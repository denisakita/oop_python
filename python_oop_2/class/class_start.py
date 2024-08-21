class Book:
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    __booklist = None

    def __init__(self, title, book_type):
        self.title = title
        if book_type not in self.BOOK_TYPES:
            raise ValueError("Invalid book type")
        self.book_type = book_type

    def set_title(self, new_title):
        self.title = new_title

    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES

    @classmethod
    def get_book_list(cls):
        if cls.__booklist is None:
            cls.__booklist = []
        return cls.__booklist


print("Book Types:", Book.get_book_types())

book1 = Book("The Great Gatsby", "HARDCOVER")
book2 = Book("Python Programming", "EBOOK")

print(book1.title)
print(book2.title)

thebooks = Book.get_book_list()
thebooks.append(book1)
thebooks.append(book2)
print([book.title for book in thebooks])
