class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def get_book(self):
        return f'Книга: {self.name} -  Автор: {self.author}'


