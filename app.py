from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html");

@app.route('/anxiety')
def one():
    return render_template("anxiety.html");

@app.route('/depression')
def two():
    return render_template("depression.html");

@app.route('/eatingdisorder')
def three():
    return render_template("eatingdisorder.html");

@app.route('/resources')
def four():
    return render_template("resources.html");

@app.route('/about')
def five():
    return render_template("about.html");
