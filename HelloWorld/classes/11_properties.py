class Product:
    def __init__(self, price):
        self.price = price

# You will want to prevent this from running because prices shouldn't be negative
# product = Product(-50)

    # Old Way is to crreate these two functions
    # def get_price(self):
    #     return self.__price

    # def get_price(self, value):
    # if value < 0:
    #     raise ValueError("Price cannot be negative")
    # self.__price = value

    # New Way

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value

    # price = property(get_price, set_price)

    product1 = Product(10)
    product2 = Product(-10)

    print(product1.price)
    print(product2.price)
