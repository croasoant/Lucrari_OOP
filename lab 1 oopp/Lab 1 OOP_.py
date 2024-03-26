class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]

    def display_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")


if __name__ == "__main__":
    library = Library()

    book1 = Book("Python Programming", "John Doe", "123456789")
    book2 = Book("Data Structures", "Jane Smith", "987654321")

    library.add_book(book1)
    library.add_book(book2)

    print("Books in the library:")
    library.display_books()

    library.remove_book("123456789")

    print("\nAfter removing a book:")
    library.display_books()