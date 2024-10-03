from Content import Content
from Product import Product


class Book(Product, Content):
    def __init__(self, name: str, author: str, genre: str, price: int):
        Product.__init__(self, name, price)
        Content.__init__(self, genre)
        self.__author = author

    def __repr__(self):
        return f'{{ "name": "{self.name}", "author": "{self.author}", "genre": "{self.genre}", "price": {self.price} }}'

    @property
    def author(self):
        return self.__author

    def set_author(self, author: str):
        if len(author) <= 0:
            raise ValueError("Author length must be greater than 0.")
        self.__author = author
