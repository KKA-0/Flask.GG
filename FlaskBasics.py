from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('intex.html')
@app.route("/about")
def harry():
    name = "harry"
    return render_template('about.html', name = name)
app.run(debug=True)