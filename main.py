from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    y = '1';
    if request.method == "POST":
        no = random.randint(1, 6);
        y = str(no);

    return render_template('index.html', x=y);


app.run()
