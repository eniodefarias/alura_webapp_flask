from flask import Flask   # pip install  flask==2.0.2
from flask import Flask, render_template, request, redirect



class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
        print(f'{self.nome} // {self.categoria} // {self.console}')


app = Flask(__name__)

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('Super Mario', 'Action', 'SNES')
jogo3 = Jogo('GTA', 'Open World', 'PC')

lista_jogos = [jogo1, jogo2, jogo3]
print(lista_jogos)


#@app.route('/inicio')
#def ola_inicio():
#    return '<p>ola mundo inicio</p>'


#@app.route('/listar')
@app.route('/')
def lista():


    #lista_jogos = ['Tetris', 'Super Mario', 'GTA']
    #return render_template('lista.html', titulo='jogos!!!')

    titulo = 'Jogoteca'


    return render_template('lista.html', titulo=titulo,  jogos=lista_jogos )

@app.route('/novo')
def novo():
    titulo = 'Cadastre um novo Jogo'
    return render_template('novo.html', titulo=titulo)



#o default é GET
@app.route('/criar', methods=['POST',])
def criar():

    nome = request.form['nome']
    print(nome)
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista_jogos.append(jogo)

    titulo = f'Adicionado Jogo "{nome}" na lista'

    #return render_template('lista.html', titulo=titulo, jogos=lista_jogos)
    return redirect('/')



#default http://127.0.0.1:5000
#app.run()

#app.run(host='0.0.0.0', port=8080)

# HINT: com o debug é ativado o modo debugerm=, assim toda vez que for feito alteração no fonte, o web ira atualizar junto
# HINT: mas se der um Excepion irá quebrar e derrubar o flak web

app.run(host='0.0.0.0', port=8080, debug=True)

