from abc import ABC, abstractmethod


class Asset(ABC):

    def __init__(self, price):
        self.price = price

    @abstractmethod
    def __str__(self):
        pass


class Stocks(Asset):
    def __init__(self, ticker, price, company_name):
        super().__init__(price)
        self.company_name = company_name
        self.ticker = ticker

    def __str__(self):
        return f'{self.ticker} {self.company_name} {self.price}'

    def __lt__(self, value):
        return self.price < value.price


class Bonds(Asset):
    def __init__(self, price, description, duration, yieldamt):
        super().__init__(price)
        self.description = description
        self.duration = duration
        self.yieldamt = yieldamt

    def __str__(self):
        return f'{self.description} {self.duration} {self.yieldamt}'

    def __lt__(self, value):
        return self.price < value.price


stocks = [
    Stocks("MSFT", 342.0, "Microsoft"),
    Stocks("Google", 456.0, "Google"),
    Stocks("AWS", 234.0, "AWS")

]

bonds = [
    Bonds(45, "USD", 34, 4),
    Bonds(46, "USD", 45, 8)
]

stocks.sort()
bonds.sort()

for stock in stocks:
    print(stock)

print("----------------------------------------")
for bond in bonds:
    print(bond)
