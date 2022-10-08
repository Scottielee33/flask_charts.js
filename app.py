from flask import Flask, render_template
import os, random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="Home")

@app.route("/challenge")
def challenge():
    qubit = random.choice(os.listdir("data/"))
    y_data = txt_to_list("data/" + qubit)
    x_data = [item for item in range(0, len(y_data))]
    answer = good_answer(qubit)
    return render_template("challenge.html", y_values=y_data, x_values=x_data, title="Challenge", answer=answer)

def txt_to_list(txt_file):
    my_file = open(txt_file, "r")
    content = my_file.read()
    content_list = content.split("\n")
    my_file.close()
    content_list.remove("")
    float_list = [float(i) for i in content_list]
    return float_list

def good_answer(qubit):
    answer = qubit.split("-")
    if answer == "singlet":
        return "zero"
    else:
        return "one"

if __name__ == "__main__":
    app.run()