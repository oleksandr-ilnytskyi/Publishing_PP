class Product:
    def __init__(self, name: str, price: int):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    def set_name(self, name: str):
        if len(name) <= 0:
            raise ValueError("Name length must be greater than 0.")
        self.__name = name

    def set_price(self, price: int):
        if price <= 0:
            raise ValueError("Price must be greater than 0.")
        self.__price = price
