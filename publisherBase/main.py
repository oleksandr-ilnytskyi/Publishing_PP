from PublishingService import PublishingService

if __name__ == '__main__':
    book1 = PublishingService.add_book("Colony", "Kidruk", "Sci-fi", 499)
    print(book1)
    sticker1 = PublishingService.add_sticker("Jessy Pinkman in the house", "Glossy", 125)
    print(sticker1)
    PublishingService.update_product(book1, price=549)
    print(book1)
    PublishingService.update_product(sticker1, name="Spaceman")
    print(sticker1)
