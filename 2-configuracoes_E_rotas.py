#configurações e 

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Index"

def teste():
    return "<h1> testando 1</h1>"

def teste2():
    return "<h2> testanto 2</h2>"

app.add_url_rule("/teste", "teste", teste)
app.add_url_rule('/teste-2', 'teste2', teste2)

if __name__ == '__main__':
    app.run(debug=True, port='3000')