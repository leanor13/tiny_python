from logic.book_service import get_all_books, get_book_by_id, add_book


def test_get_all_books():
    add_book({"id":1, "title":"hello"})
    all_books = get_all_books()
    print(all_books)

def test_get_book_by_id():
    book_1 = get_book_by_id(1)
    if book_1:
        print(book_1.__dict__)
    else:
        print("not found")

def test_get_book_by_genre():
    add_book({"id":2, "title":"hello"})
    add_book({"id":3, "title":"hello", "genre":"fiction"})
    result1 = get_all_books(genre = "unknown")
    print("Unknown: ", result1)
    result2 = get_all_books(genre = "fiction")
    print("fiction ", result2)
    result3 = get_all_books(genre = "bhb")
    print("dsbhdjs: ", result3)

test_get_all_books()
test_get_book_by_id()
test_get_book_by_genre()