class Book:
    def __init__(self, id: int, name: str, pages:int):
        self.id = id
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f"Книга {self.name!r}"

    def __repr__(self) -> str:
        return f"Book(id = {self.id}, name = {self.name!r}, pages = {self.pages})"

book1 = Book(112233, "Фауст", 500)
print(str(book1))
print(repr(book1))

class Library:
    def __init__(self, books: list):
        self.books = books

    def get_next_book_id(self):
        if len(self.books) == 0:
            index = 1
        index = len(self.books) + 1
        return index

    def get_index_by_book_id(self, book_name: str):
        if book_name in self.books:
            return self.books.index(book_name) + 1
        else:
            raise ValueError("Книги с запрашиваемым id не существует")

library = Library(["Фауст","Гамлет", "Маленький принц"])
print(library.get_next_book_id())
print(library.get_index_by_book_id("Гамлет"))