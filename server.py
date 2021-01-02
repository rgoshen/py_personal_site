from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    """
    Renders the home page.
    """
    return 'Hello World!'


if __name__ == "__main__":
    app.run(debug=True)
