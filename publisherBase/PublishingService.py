from Book import Book
from Content import Content
from Sticker import Sticker
from Product import Product


class PublishingService:
    def add_book(name: str, author: str, genre: str, price: int):
        return Book(name, author, genre, price)

    def add_sticker(name: str, material: str, price: int):
        return Sticker(name, material, price)

    def update_product(product: Product, name: str = "", price: int = 0):
        if len(name) > 0:
            product.set_name(name)
        if price > 0:
            product.set_price(price)


PublishingService.add_book = staticmethod(PublishingService.add_book)
PublishingService.add_sticker = staticmethod(PublishingService.add_sticker)
PublishingService.update_product = staticmethod(PublishingService.update_product)
