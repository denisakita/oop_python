from abc import ABC, abstractmethod


class Structure(ABC):

    def __init__(self, price):
        self.price = price

    @abstractmethod
    def get_description(self):
        return "This is a description"


class Stocks(Structure):
    def __init__(self, company_name, price, ticker):
        super().__init__(price)
        self.company_name = company_name
        self.ticker = ticker

    def get_description(self):
        return f"{self.ticker}: {self.company_name} -- ${self.price}"


class Bonds(Structure):
    def __init__(self, price, description, duration, yeld):
        super().__init__(price)
        self.description = description
        self.duration = duration
        self.yeld = yeld

    def get_description(self):
        return f"{"Description"} :{self.description} : {self.duration} : ${self.price} : {self.yeld}"


msft = Stocks("MSFT", 342.0, "Microsoft")
goog = Stocks("Google", 456.0, "Google")

us1 = Bonds(45, "USD", 34, 4)
us2 = Bonds(46, "USD", 45, 8)

print(msft.get_description())
print(goog.get_description())

print(us1.get_description())
print(us2.get_description())


