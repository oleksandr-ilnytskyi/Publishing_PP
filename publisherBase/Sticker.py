from Product import Product


class Sticker(Product):
    def __init__(self, name: str, material: str, price: int):
        Product.__init__(self, name, price)
        self.__material = material

    def __repr__(self):
        return f'{{ "name": "{self.name}", "material": "{self.material}", "price": {self.price} }}'

    @property
    def material(self):
        return self.__material

    def set_material(self, material: str):
        if len(material) <= 0:
            raise ValueError("Material length must be greater than 0.")
        self.__material = material
