ALLOWED_GENRES = {"fiction", "ski-fi", "unknown"}
MAX_TITLE_LEN = 256
MAX_AUTHOR_LEN = 64
FIRST_PUBLICATION_YEAR = 0
# we allow future publications
LAST_PUBLICATION_YEAR = 3000

class Book:
    def __init__(self,
                 id: int,
                 title: str,
                 author: str = "",
                 published_year: int | None = None,
                 genre: str = "unknown"):
        if id <= 0:
            raise ValueError("Id should not be negative")
        if not title.strip():
            raise ValueError("Title is required")
        if len(title) > MAX_TITLE_LEN:
            raise ValueError("Title too long")
        if author and len(author) > MAX_AUTHOR_LEN:
            raise ValueError("Author too long")
        if published_year is not None and published_year not in range(FIRST_PUBLICATION_YEAR, LAST_PUBLICATION_YEAR +\
                1):
            raise ValueError("publication year not in allowed range")
        if not genre:
            genre = "unknown"
        if genre and genre not in ALLOWED_GENRES:
            raise ValueError("genre not in allowed list")


        self.id = id
        self.title = title
        self.author = author
        self.published_year = published_year
        self.genre = genre

    def __repr__(self):
        return f"Book(id={self.id}, title={self.title}, genre={self.genre}, author={self.author}"