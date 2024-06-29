from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Goodbye, World!</h1>"

app.run(debug=True)