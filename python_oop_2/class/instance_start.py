""" Create a basic class"""


class Book():
    """ the "init" function is called when the instance is created
    and ready to be initialized"""

    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is secret attribute"

    """ Create instance methods"""

    def get_price(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def set_discount(self, amount):
        self._discount = amount


""" Create instances of the class"""

book1 = Book("Test1", "TestAuthor", 200, 1000)
book2 = Book("Test2", "TestAuthor", 300, 1500)

""" Print the class and property"""
print(book1.get_price())
book1.set_discount(0.25)
print(book1.get_price())

print(book2._Book__secret)
