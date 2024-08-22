class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f' {self.title}, by {self.author}, costs: {self.price}'

    def __repr__(self):
        return f"Book(title={self.title}, author={self.author}, price={self.price})"


b1 = Book('Python', 'Test', 5.0)
print(b1.__str__())
print(b1.__repr__())
print("----------------------------------------------")
print(str(b1))
print(repr(b1))
