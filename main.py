from flask import Flask
from flask.templating import render_template
app = Flask(__name__)
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

app.run(debug=True)
