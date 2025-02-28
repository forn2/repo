# TODO написать класс Book

# TODO написать класс Library
BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"

class Library:
    def __init__(self, books=None):
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Returns the next available book ID.
        """
        if not self.books:
            return 1
        return max(book.id for book in self.books) + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Returns the index of a book with the given ID in the library.

        Args:
            book_id (int): The ID of the book to find.

        Returns:
            int: The index of the book in the list.

        Raises:
            ValueError: If the book with the given ID is not found.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError(f"Book with ID {book_id} not found")

if __name__ == '__main__':
    empty_library = Library()  # Initialize an empty library
    print(empty_library.get_next_book_id())  # Check the next ID for an empty library

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # Initialize a library with books
    print(library_with_books.get_next_book_id())  # Check the next ID for a non-empty library

    print(library_with_books.get_index_by_book_id(1))  # Check the index of the book with ID 1
