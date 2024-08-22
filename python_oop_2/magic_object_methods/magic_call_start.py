class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self.discount = 0.1

    def __str__(self):
        return f' {self.title}, by {self.author}, costs: {self.price}'

    def __call__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


b1 = Book('Python', 'Test', 5.0)
print(b1)
b1(title='Angular', author='Test', price=5.0)
print(b1)
