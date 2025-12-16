from flask import Flask, render_template, request, redirect, url_for
from Gerenciador import Gerencia

app = Flask(__name__)
gerenciador = Gerencia()

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():

    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        prioridade = int(request.form['prioridade'])
        gerenciador.adicionando_atividade(titulo, descricao, prioridade)
        return redirect(url_for('index'))
    return render_template('adicionar.html')

@app.route('/concluir')
def concluir():

    gerenciador.concluir_atividade_prioridade()
    return redirect(url_for('index'))

@app.route('/listar_prioridade')
def listar_prioridade():

    atividades = gerenciador.get_prioridades()
    return render_template('lista.html', titulo="Atividades por Prioridade", atividades=atividades)

@app.route('/listar_atividades')
def listar_atividades():

    atividades = gerenciador.get_atividades()
    return render_template('lista.html', titulo="Todas as Atividades", atividades=atividades)

@app.route('/historico')
def historico():

    atividades = gerenciador.get_historico()
    return render_template('lista.html', titulo="Histórico de Atividades Concluídas", atividades=atividades)

if __name__ == '__main__':
    app.run(debug=True)