from flask import Flask, render_template, request

app = Flask('app')

users = ["Boss", "NMB", "BKDUS"]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/process', methods=['POST'])
def process():
    input_field = request.form.get('input_field')
    return render_template("process.html",)

app.run(host='0.0.0.0', port=8080)
