from fastapi import APIRouter, HTTPException
from database.fake_db import books
from schemas.book_schema import Book, UpdateBook

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)


# 1. Get all books
@router.get("/")
def get_books():
    return books


# 2. Get single book
@router.get("/{book_id}")
def get_book(book_id: int):

    for book in books:
        if book["id"] == book_id:
            return book

    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )


# 3. Add new book
@router.post("/")
def add_book(book: Book):

    books.append(book.dict())

    return {
        "message": "Book added successfully",
        "book": book
    }


# 4. Update book
@router.put("/{book_id}")
def update_book(book_id: int, updated_book: UpdateBook):

    for book in books:

        if book["id"] == book_id:

            if updated_book.title is not None:
                book["title"] = updated_book.title

            if updated_book.author is not None:
                book["author"] = updated_book.author

            if updated_book.price is not None:
                book["price"] = updated_book.price

            if updated_book.category is not None:
                book["category"] = updated_book.category

            return {
                "message": "Book updated successfully",
                "book": book
            }

    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )


# 5. Delete book
@router.delete("/{book_id}")
def delete_book(book_id: int):

    for book in books:

        if book["id"] == book_id:

            books.remove(book)

            return {
                "message": "Book deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )


# 6. Search by title
@router.get("/search/{title}")
def search_book(title: str):

    result = []

    for book in books:

        if title.lower() in book["title"].lower():
            result.append(book)

    return result


# 7. Filter by author
@router.get("/author/{author_name}")
def get_books_by_author(author_name: str):

    result = []

    for book in books:

        if author_name.lower() == book["author"].lower():
            result.append(book)

    return result


# 8. Filter by category
@router.get("/category/{category_name}")
def get_books_by_category(category_name: str):

    result = []

    for book in books:

        if category_name.lower() == book["category"].lower():
            result.append(book)

    return result