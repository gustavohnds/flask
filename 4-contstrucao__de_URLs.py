# construcao de URLs, redirecionamento

# 2 funcoes a mais: redirect e url_for
# url_for - para construir os URLs

from flask import Flask, redirect, url_for

app = Flask(__name__)

#code

@app.route('/admin')
def admin():
    return '<h1>Admin</h1>'

@app.route('/guest/<guest>')
def guest(guest):
    return "<p>Olá usuário <b>{}</b>!</p>".format(guest)

@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest', guest=name))

@app.route('/google')
def google():
    return redirect('http://google.com.br')

if __name__ == '__main__':
    app.run(debug=True)
