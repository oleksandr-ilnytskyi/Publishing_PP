class Content:
    def __init__(self, genre: str):
        self.__genre = genre

    @property
    def genre(self):
        return self.__genre

    def set_genre(self, genre: str):
        if len(genre) <= 0:
            raise ValueError("Genre length must be greater than 0.")
        self.__genre = genre
