from fastapi import FastAPI
from shemas import Book

app = FastAPI()


@app.get('/')
def home():
    return {'key': 'hello'}


@app.get('/{pk}')
def get_pk(pk: int):
    return {'key': pk}


@app.post('/post', response_model=Book)
def create_book(book: Book):
    return book
