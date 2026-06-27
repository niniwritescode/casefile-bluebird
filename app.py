from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/casefile")
def casefile():
    return render_template("casefile.html")

@app.route("/suspects")
def suspects():
    return render_template("suspects.html")

@app.route("/witnesses")
def witnesses():
    return render_template("witnesses.html")

@app.route("/evidence")
def evidence():
    return render_template("evidence.html")

@app.route("/victim")
def victim():
    return render_template("victim.html")

@app.route("/breaking")
def breaking():
    return render_template("breaking.html")

@app.route("/summary")
def summary():
    return render_template("summary.html")

@app.route("/accuse")
def accuse():
    return render_template("accuse.html")

@app.route("/journal")
def journal():
    return render_template("journal.html")
@app.route("/about")
def about():
    return render_template("about.html")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)