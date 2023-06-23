from turtle import color
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return 'Home'

@app.route('/play')
def play_1():
    return render_template('index.html', num=3, color="blue")

@app.route('/play/<int:num>')
def play_2(num):
    return render_template('index.html', num=num, color="blue")

@app.route('/play/<int:num>/<string:color>')
def play_3(num):
    return render_template('index.html', num=num, color=color)

if __name__ == "__main__":
    app.run(debug=True)