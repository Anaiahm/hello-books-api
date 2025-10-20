from flask import abort, Blueprint, make_response
from app.models.book import books

book_bp = Blueprint("books", __name__, url_prefix="/books")

@book_bp.get("")
def get_all_books():
    books_response = []
    for book in books:
        books_response.append(
            {
                "id": book.id,
                "title": book.title,
                "description": book.description
            }
        )
    return books_response

@book_bp.get("/<book_id>")
def get_specific_book(book_id):
    book = validate_book(book_id)
    book_info = {
        "id": book.id,
        "title": book.title,
        "description": book.description 
    }
    return book_info

def validate_book(book_id):
    try:
        book_id = int(book_id)
    except:
        response = {"message": f"book {book_id} invalid"}
        abort(make_response(response, 400))

    for book in books:
        if book.id == book_id:
            return book

    response = {"message": f"book {book_id} not found"}
    abort(make_response(response, 404))