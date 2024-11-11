from book import Book

book1 = Book('Малыш', 'Стругацкие А. и Б.')
book2 = Book('Fight Club', 'Palahniuk')
book3 = Book('The Odyssey', 'Homer')
library = [book1, book2, book3]

for book in library:
    print(book.get_book())