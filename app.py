from flask import Flask, request, jsonify

app = Flask(__name__)

# TEMP DATA
books = [
    {
        "id": 1,
        "title": "Python Basics",
        "author": "John Smith",
        "year": 2024
    },
    {
        "id": 2,
        "title": "Flask Guide",
        "author": "Jane Doe",
        "year": 2023
    }
]

# HOME PAGE
@app.route("/")
def home():
    return """
    <h1>Online Library Backend Working</h1>
    <p>Flask server is running successfully.</p>
    """

# GET ALL BOOKS
@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books)

# GET ONE BOOK
@app.route("/books/<int:id>", methods=["GET"])
def get_book(id):

    for book in books:
        if book["id"] == id:
            return jsonify(book)

    return jsonify({
        "error": "Book not found"
    }), 404
 
# ADD BOOK
@app.route("/books", methods=["POST"])
def add_book():

    new_book = request.json

    books.append(new_book)

    return jsonify({
        "message": "Book added",
        "book": new_book
    }), 201

# DELETE BOOK
@app.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):

    for book in books:
        if book["id"] == id:
            books.remove(book)

            return jsonify({
                "message": "Book deleted"
            })

    return jsonify({
        "error": "Book not found"
    }), 404

if __name__ == "__main__":
    app.run(debug=True)