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

