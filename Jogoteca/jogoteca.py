# Importando o framework Flask
from flask import Flask, render_template, request, redirect # type: ignore
# Importar classe jogo
from modelos.jogo import Jogo

# Criando a aplicação
app = Flask(__name__)

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
    
# Rodar a aplicação
app.run(debug=True)