from flask import Flask, render_template, session, redirect, request 
app = Flask(__name__)
app.secret_key = "casey"

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    return render_template('index.html')

@app.route('/add_visit')
def add_visit():
    session['count'] += 1
    return redirect('/')

@app.route('/add_two')
def add_two():
    session['count'] += 2
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

@app.route('/count_adjust', methods=["POST"])
def change_count_amount():
    session['count'] += int(request.form["counter"])
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)