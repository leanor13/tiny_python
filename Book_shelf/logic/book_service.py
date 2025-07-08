from domain.book import Book

BOOK_STORAGE: list[Book] = []

def add_book(data: dict) -> Book:
    book = Book(id = data.get("id"),
                title=data.get("title"),
                author=data.get("author"),
                published_year=data.get("published_year"),
                genre=data.get("genre"))
    BOOK_STORAGE.append(book)
    return book

def get_all_books(**kwargs) -> list[Book]:
    if "genre" in kwargs.keys():
        #if no such book return empty list
        final_list = [book for book in BOOK_STORAGE if book.genre == kwargs["genre"]]
    else:
        final_list = BOOK_STORAGE
    return final_list

def get_book_by_id(id: int) -> Book | None:
    for book in BOOK_STORAGE:
        if book.id == id:
            return book
    return None

