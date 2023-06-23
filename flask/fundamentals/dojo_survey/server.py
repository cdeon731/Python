from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)

app.secret_key = "casey was here"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['name']: request.form['name']
    session['location']: request.form['location']
    session['language']: request.form['language']
    session['comments']: request.form['comments']
    session['age']: request.form['age']
    session['experience']: request.form['experience']
    return redirect('/success')

@app.route('/success')
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)