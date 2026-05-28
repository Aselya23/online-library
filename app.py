from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<h1>📚 Online Library Backend Working</h1>
<p>Flask server is running successfully.</p>
"""

if __name__ == "__main__":
    app.run(debug=True)