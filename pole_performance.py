from flask import Flask, render_template
app = Flask(__name__)


@app.route("/pp1")
def shield_homepage():
    return render_template('shield_home.html')


@app.route("/pp2")
def lightwave_homepage():
    return render_template('lightwave_home.html')


if __name__ == "__main__":
    app.run()
