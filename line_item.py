class LineItem:
    def __init__(self, sku: str, price: float, amount: int):
        self.sku = sku
        self.price = price
        self.amount = amount

    @property  # Computed Property
    def value(self):
        return self.price * self.amount

    @property  # Getter
    def sku(self):
        return self._sku

    @sku.setter  # Setter
    def sku(self, value):
        value = value.strip()
        if not value:
            raise ValueError(f'empty sku: {value!r}')
        self._sku = value


l1 = LineItem('S01E01', 1.2, 100)
print(l1.value)
print(l1.sku)

# Invalid
l1.sku = ''
