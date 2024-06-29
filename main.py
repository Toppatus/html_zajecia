from flask import Flask

app = Flask(__name__)

print(__name__)

@app.route("/")
def hello_world():
    return "<h1>Goodbye, World!</h1>"

@app.route("/podstrona")
def podstrona():
    return "<h1>Jakaś podstrona </h1>"

app.run(debug=True)