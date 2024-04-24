# Importando o framework Flask
from flask import Flask, render_template # type: ignore
# Importar classe jogo
from modelos.jogo import Jogo

# Criando a aplicação
app = Flask(__name__)

# Criar uma rota
@app.route('/inicio')
def ola():
    jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
    jogo2 = Jogo('Valorant', 'FPS', 'PC')
    jogo3 = Jogo('MTG Arena', 'Card Game', 'PC')
    lista = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='Jogos', jogos=lista)
# Rodar a aplicação
app.run()