from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder="../templates"
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return """
    <h1>About Page</h1>
    <p>This site is deployed with Flask + Vercel</p>
    """

# Vercel이 app 객체를 인식
app = app
