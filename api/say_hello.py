from flask import Flask, render_template, request
from __main__ import app


@app.route("/hello/<path:name>", methods=["GET"])
def say_hello(name):
    return render_template("hello.html", name=name)
