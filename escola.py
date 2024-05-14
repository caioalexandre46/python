from flask import Flask, render_template, request, redirect, url_for, flash, session

class Aluno:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.uf = email
aluno1 = Aluno('Fabiano','66999537642','fabianotaguchi@gmail.com')
lista = [aluno1]

class Usuario:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha
usuario1 = Usuario('caio','caio')
listaUsuario = [usuario1]

app = Flask(__name__)
app.secret_key = 'teste123'

@app.route('/')
def index():
    return render_template('lista.html', titulo='Listagem de alunos', alunos=lista)

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/novo')
def novo():
    if 'usuarioLogado' not in session or session['usuarioLogado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Cadastro de um novo time')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    if usuario in usuarios:
        usuario_obj = usuarios[usuario]
        if senha == usuario_obj.senha:
            session['usuarioLogado'] = usuario_obj.login
            flash(usuario_obj.login + ' logado com sucesso!')
            proximaPagina = request.form.get('proxima')
            if proximaPagina:
                return redirect(proximaPagina)
            else:
                return redirect(url_for('index'))
        else:
            flash('Senha incorreta.')
    else:
        flash('Usuário não encontrado.')
    return redirect(url_for('login'))

@app.route('/criar', methods=['POST',])
def criar():
    nome = request. form['nome']
    email = request. form['email']
    telefone = request. form['telefone']
    aluno = Aluno(nome, telefone, email)
    lista.append(aluno)
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session['usuarioLogado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))

app.run(debug=True)

                 
   
