from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/Blog")
def blog():
    return "Hello this is my blog"

@app.route("/Resume")
def resume():
    return "Hello this is my resume"

if __name__ == "__main__":
    app.run(debug=True)