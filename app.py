from flask import Flask, render_template
from return_div import return_div
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Create flask instance
app = Flask(__name__)

app.config["SECRET_KEY"] = "123"


# Create a URL route in our application for "/"
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/plot.html", methods=["GET", "POST"])
def plot():
    return render_template("plot.html", plot=return_div(1))


@app.route("/team.html")
def team():
    return render_template("team.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
