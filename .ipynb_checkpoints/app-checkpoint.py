from flask import Flask

app= Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, Flask</h1>"

@app.route("/about")
def about():
    return "<h2>this all about the about</h2>"


if __name__=="__main__":
    app.run(debug=True)