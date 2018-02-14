from bottle import route, run
from bottle import request, template
from bottle import TEMPLATE_PATH, static_file
from bottle import get, error

import os, sys

TEMPLATE_PATH.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "views")))

dirname = os.path.dirname(sys.argv[0])

#html = '<center><h1> Olá </h1></center>'
'''
@route('/user/<nome>/<id>')
@route('/') #aplicacao deve interpretar um determinado caminho. Neste caso, estou ligando o caminho barra hello à funcao index
def index(id, nome = 'Desconhecido'):
    return '<center><h1> Olá ' + nome + ' seu id é ' + id + '</h1></center>' #retorno enviado ao navegador


@route('/python') #aplicacao deve interpretar um determinado caminho. Neste caso, estou ligando o caminho barra python à funcao python
def python():
    return '<h1> Curso Python</h1>' #retorno enviado ao navegador

'''

# static routes
@get('/static/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root=dirname+'/static/css')

@get('/static/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root=dirname+'/static/js')

@get('/static/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root=dirname+'/static/img')

@get('/static/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root=dirname+'/static/fonts')


@route('/login') # @get('/login')
def login():
    return template('login')

def check_login(username, password):
    d = {'daniel':'python', 'pri':'to', 'andre':'bio'}
    if username in d.keys() and d[username] == password:
        return True
    return False


@route('/login', method='POST') # @post('/login')
def acao_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    return template('verificacao_login', sucesso=check_login(username,password), nome=username)

@error(404)
def error404(error):
    return template('pagina404')

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True) # Quando for colocar em produção, Debug = False

