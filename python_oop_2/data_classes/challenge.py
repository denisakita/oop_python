from abc import ABC, abstractmethod

from dataclasses import dataclass


@dataclass
class Asset(ABC):
    price: float

    @abstractmethod
    def __lt__(self, other):
        pass


@dataclass
class Stocks(Asset):
    ticker: str
    company_name: str

    def __lt__(self, other):
        return self.price < other.price

    def __str__(self):
        return f'{self.ticker} {self.company_name} {self.price}'


@dataclass
class Bonds(Asset):
    description: str
    duration: int
    yieldamt: float

    def __str__(self):
        return f'{self.description} {self.duration} {self.yieldamt}'

    def __lt__(self, other):
        return self.price < other.price


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
