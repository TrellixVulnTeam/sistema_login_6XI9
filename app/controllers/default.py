from app import app
from bottle import request, template
from bottle import static_file
from bottle import error

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
@app.get('/static/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root=aux_dirname+'/static/css')

@app.get('/static/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root=aux_dirname+'/static/js')

@app.get('/static/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root=aux_dirname+'/static/img')

@app.get('/static/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root=aux_dirname+'/static/fonts')

@app.route('/') # @get('/')
def login():
    return template('login')

@app.route('/cadastro')
def cadastro():
    return template('cadastro')

@app.route('/cadastro', method='POST')
def acao_cadastro():
    username = request.forms.get('username')
    password = request.forms.get('password')
    insert_user(username, password)
    return template('verificacao_cadastro', nome=username)

@app.route('/', method='POST') # @post('/')
def acao_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    return template('verificacao_login', sucesso=True)

@app.error(404)
def error404(error):
    return template('pagina404')
