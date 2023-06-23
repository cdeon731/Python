from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template ('index.html', row=4,col=4,color_one='red',color_two='black')

@app.route('/<int:x>/<int:y>/<string:one>/<string:two>')
def row_col_two(x,y,one,two):
    return render_template("index.html",row=x,col=y,color_one=one,color_two=two)

if __name__=="__main__":
    app.run(debug=True)