from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/prompt", methods=["POST"])
def prompt():
    text = request.form["text"]
    speed = int(request.form["speed"])
    size = int(request.form["size"])
    return render_template("prompt.html", text=text, speed=speed, size=size)


if __name__ == "__main__":
    app.run(debug=True)
