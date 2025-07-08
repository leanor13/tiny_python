from logic.book_service import add_book

def test_add_book():
    data = {
        "id": 1,
        "title": "Test Book",
        "author": "Test Author",
        "published_year": 2023,
        "genre": "unknown"
    }

    book = add_book(data)
    print(book.__dict__)

test_add_book()