class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self.discount = 0.1

    def __str__(self):
        return f' {self.title}, by {self.author}, costs: {self.price}'

    def __getattribute__(self, name):
        if name == "price":
            p = super().__getattribute__("price")
            d = super().__getattribute__("discount")
            return p - (d * p)
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        if name == "price":
            if type(value) is not float:
                raise TypeError("value must be float")
        return super().__setattr__(name, value)

    def __getattr__(self, name):
        return name + " is not here"


b1 = Book('Python', 'Test', 5.0)
b1.price = 2.0
print(b1.price)
print(b1.randomprop)
