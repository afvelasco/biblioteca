from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hola, si funciona desde casa "

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/')
def actualizar():("actualizar.html")



if __name__=='__main__':
    app.run(host="0.0.0.0", debug=True,port="8000")