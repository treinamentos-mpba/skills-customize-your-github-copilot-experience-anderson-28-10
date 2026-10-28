from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="School Library API")


class BookCreate(BaseModel):
    title: str
    author: str


class Book(BookCreate):
    id: int


books: dict[int, Book] = {
    1: Book(id=1, title="The Hobbit", author="J. R. R. Tolkien"),
    2: Book(id=2, title="A Wizard of Earthsea", author="Ursula K. Le Guin"),
}


@app.get("/")
def read_root():
    return {"message": "Welcome to the School Library API"}


@app.get("/books", response_model=list[Book])
def list_books():
    # TODO: Return all books.
    raise HTTPException(status_code=501, detail="Implement this endpoint")


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    # TODO: Find and return the requested book, or raise a 404 error.
    raise HTTPException(status_code=501, detail="Implement this endpoint")


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_data: BookCreate):
    # TODO: Assign an ID, save the book, and return it.
    raise HTTPException(status_code=501, detail="Implement this endpoint")


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_data: BookCreate):
    # TODO: Update the requested book, or raise a 404 error.
    raise HTTPException(status_code=501, detail="Implement this endpoint")


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    # TODO: Delete the requested book, or raise a 404 error.
    raise HTTPException(status_code=501, detail="Implement this endpoint")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)