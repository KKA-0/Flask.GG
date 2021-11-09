from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world whatuppp fuk u!"
app.run()