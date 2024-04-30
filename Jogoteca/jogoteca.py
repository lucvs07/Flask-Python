# Importando o framework Flask
from flask import Flask, render_template, request, redirect, session, flash, url_for # type: ignore
# Importar classe jogo
from modelos.jogo import Jogo
from modelos.usuario import Usuario

# Criando a aplicação
app = Flask(__name__)
app.secret_key = 'alura'

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('Valorant', 'FPS', 'PC')
jogo3 = Jogo('MTG Arena', 'Card Game', 'PC')
lista = [jogo1, jogo2, jogo3]

usuario1 = Usuario('Lucas', 'Kingue', 'Alohomora')
usuario2 = Usuario('Giulia', 'Giubs', 'Amomeunamorado')
usuario3 = Usuario('Irineu', '404', 'naolembro')

usuarios = {usuario1._nickname : usuario1,
            usuario2._nickname : usuario2,
            usuario3._nickname : usuario3}
# Criar uma rota
@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Cadastrar Novo Jogo')

@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios [request.form['usuario']]
        if request.form['senha'] == usuario._senha:
            session['usuario_logado'] = usuario._nickname
            flash(f'{usuario._nickname} logado com sucesso')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuario não logado')
        return redirect(url_for('login'))
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash(f'Logout efetuado com sucesso !')
    return redirect(url_for('index'))
            
# Rodar a aplicação
app.run(debug=True)