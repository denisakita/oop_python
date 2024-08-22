class Stock:
    def __init__(self, ticker: str, price: float, company: str) -> None:
        self.ticker = ticker
        self.price = price
        self.company = company

    def get_description(self):
        return f"{self.ticker}: {self.company} -- {self.price}"


msft = Stock("MSFT", "$4000", "MSFT")
goog = Stock("GOOG", "2000", "GOOG")
amzn = Stock("AMZN", "3000", "AMZN")

print(msft.get_description())
print(goog.get_description())
print(amzn.get_description())
