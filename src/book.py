class Book:
    def __init__(
        self,
        title: str,
        author: str,
        year: int,
        genre: str,
        isbn: str,
    ) -> None:

        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn


class BookCollection:
    def __init__(self) -> None:
        self._books: list[Book] = []
    
    def __getitem__(self, key: int | slice) -> Book | list[Book]:
        return self._books[key]
    
    def __iter__(self):
        return iter(self._books)
    
    def __len__(self) -> int:
        return len(self._books)
    
    def add(self, book: Book) -> None:
        self._books.append(book)
    
    def remove(self, book: Book) -> None:
        self._books.remove(book)

