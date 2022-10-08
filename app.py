from flask import Flask, render_template, json

app = Flask(__name__)

@app.route("/")
def index():
    y_data = txt_to_list("data/singlet-trace-1.txt")
    x_data = [item for item in range(0, len(y_data))]
    return render_template("index.html", y_values=y_data, x_values=x_data)

def txt_to_list(txt_file):
    my_file = open(txt_file, "r")
    content = my_file.read()
    content_list = content.split("\n")
    my_file.close()
    content_list.remove("")
    float_list = [float(i) for i in content_list]
    return float_list

if __name__ == "__main__":
    app.run()