from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/Blog")
def blog():
    return "Hello this is my blog"

@app.route("/Resume")
def resume():
    return render_template("resume.html")

@app.route("/one-page")
def one_page():
    """
    temp route for seeing what the resume should look like
    """
    return render_template("one-page-resume.html")

if __name__ == "__main__":
    app.run(debug=True)
