from flask import Flask, render_template, request
from markupsafe import escape
import requests


app = Flask(__name__)
import api.say_hello


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        word = request.form["word"]
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()[0]
            return render_template("index.html", response=data)
        elif response.status_code == 404:
            return render_template(
                "index.html", error="Word not found, please try with another word."
            )
        else:
            print("Request failed with status code:", response.status_code)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
