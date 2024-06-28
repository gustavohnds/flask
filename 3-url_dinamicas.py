#criando URL dinamicas
#exemplo: 
#github/gustavoghnds
#github/hvescovi

from flask import Flask 
app = Flask(__name__)

#ex: 
#/hello/gustavo
#/hello/hylson

@app.route("/hello/<nome>")
def hello(nome):
    return "<h>Hello {}</h1>".format(nome)

#com int
@app.route("/pagina/")
@app.route("/pagina/<int:postID>")
def pagina(postID):
    if postID >= -1:
        return 'pagina {}'.format(postID)
    else:
        return 'pagina Todo'

#com float
@app.route("/pagina/<float:postID>")
def pagina2float(postID):
    if postID >= -1:
        return 'pagina {}'.format(postID)
    else:
        return 'pagina Todo'

if __name__ == '__main__':
    app.run(debug=True)