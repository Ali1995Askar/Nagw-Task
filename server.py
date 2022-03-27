from flask import Flask, request, jsonify
import helpers


app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False


@app.get('/api/books')
def books():
   return helpers.get_books(request)


@app.post('/api/books')
def create():
   return helpers.create_book(request)


@app.put('/api/books')
def update():
   return helpers.update_book(request)


@app.delete('/api/books')
def delete():
   return helpers.delete_book(request)


@app.get("/")
def docs():
   return helpers.api_docs(request)



