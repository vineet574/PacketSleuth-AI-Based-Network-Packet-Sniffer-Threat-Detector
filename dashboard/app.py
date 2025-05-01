from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def index():
    # Dummy data, replace with live stats
    return render_template("index.html", count=random.randint(1, 100))

if __name__ == "__main__":
    app.run(debug=True)
