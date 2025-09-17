import os
from flask import Flask, render_template, request

# Tell Flask to look for templates in the same folder as app.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=BASE_DIR)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet", methods=["POST"])
def greet():
    name = request.form.get("name")
    return render_template("greetings.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
