from ast import keyword
import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        name1 = request.form["name1"]
        name2 = request.form["name2"]
        keyword = request.form["keyword"]

        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=generate_prompt(name1, name2, keyword),
            temperature=0.7,
            max_tokens=4000


        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(name1, name2, keyword):
    return """Write a descriptive {}   between


Name: {} and partner is {} 
Names:""".format(
        keyword.capitalize(), name1.capitalize(), name2.capitalize()
    )
