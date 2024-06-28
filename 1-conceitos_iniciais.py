#instalando flask

#importa Flask da biblioteca flask
from flask import Flask

app = Flask(__name__) 

#cria uma rota que retorna algo
@app.route("/")
def index():
    return "Index"

#cria uma rota chamada "teste"
@app.route("/teste")
def teste():
    return "teste"

#executa
if __name__ == '__main__':
    app.run()