# Importando o framework Flask
from flask import Flask, render_template, request, redirect, session, flash # type: ignore
# Importar classe jogo
from modelos.jogo import Jogo

# Criando a aplicação
app = Flask(__name__)
app.secret_key = 'alura'

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('Valorant', 'FPS', 'PC')
jogo3 = Jogo('MTG Arena', 'Card Game', 'PC')
lista = [jogo1, jogo2, jogo3]
# Criar uma rota
@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Cadastrar Novo Jogo')

@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if 'alohomora' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(f"Usuário: {session['usuario_logado']} logado com sucesso")
        return redirect('/')
    else:
        flash('Usuário não logado')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash(f'Logout efetuado com sucesso !')
    return redirect('/')
            
# Rodar a aplicação
app.run(debug=True)