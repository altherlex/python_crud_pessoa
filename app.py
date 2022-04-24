import os
from flask import Flask, request, render_template, jsonify

from settings import APP_FOLDER
from cadastrar import cadastrar_pessoas2, cadastrar_contatos2
from consultar import consultar_pessoas2, consultar_contatos2, consultar_pessoas_contatos2
from atualizar import atualizar_pessoas2, atualizar_contatos_telefone2, atualizar_contatos_email2
from deletar import deletar_pessoas2, deletar_contatos2
from db import mysql


app = Flask(__name__)
app.config.from_pyfile(os.path.join(APP_FOLDER, "settings.py"))
mysql.init_app(app)

@app.route('/index', methods=['GET'])
@app.route('/', methods=['GET'])
def index():
    return render_template('main.html')


@app.route('/pessoas', methods=['GET'])
def cadastrar_pessoas0():
    return render_template('pessoas.html')


@app.route('/pessoas', methods=['POST'])
def cadastrar_pessoas1():
    nome = request.form['id_nome']
    cpf = request.form['id_cpf']
    return cadastrar_pessoas2(nome, cpf)


@app.route('/contatos', methods=['GET'])
def cadastrar_contatos0():
    return render_template('contatos.html')


@app.route('/contatos', methods=['POST'])
def cadastrar_contatos1():
    id_pessoas = request.form['id_pessoas']
    telefone = request.form['id_telefone']
    email = request.form['id_email']
    return cadastrar_contatos2(id_pessoas, telefone, email)


@app.route('/pessoas-cadastradas', methods=['GET'])
def consultar_pessoas1():
    return consultar_pessoas2()


@app.route('/contatos-cadastrados', methods=['GET'])
def consultar_contatos1():
    return consultar_contatos2()


@app.route('/pessoas-contatos-cadastrados', methods=['GET'])
def consultar_pessoas_contatos1():
    return consultar_pessoas_contatos2()


@app.route('/pessoas-atualizar', methods=['GET'])
def atualizar_pessoas0():
    return render_template('pessoas_atualizar.html')


@app.route('/pessoas-atualizar', methods=['POST'])
def atualizar_pessoas1():
    nome = request.form['id_nome_atualizar']
    cpf = request.form['id_cpf_atualizar']
    return atualizar_pessoas2(nome, cpf)


@app.route('/contatos-atualizar-telefone', methods=['GET'])
def atualizar_contatos_telefone0():
    return render_template('contatos_atualizar_telefone.html')


@app.route('/contatos-atualizar-telefone', methods=['POST'])
def atualizar_contatos_telefone1():
    telefone = request.form['id_telefone_atualizar']
    cpf = request.form['id_cpf_atualizar']
    return atualizar_contatos_telefone2(telefone, cpf)


@app.route('/contatos-atualizar-email', methods=['GET'])
def atualizar_contatos_email0():
    return render_template('contatos_atualizar_email.html')


@app.route('/contatos-atualizar-email', methods=['POST'])
def atualizar_contatos_email1():
    email = request.form['id_email_atualizar']
    cpf = request.form['id_cpf_atualizar']
    return atualizar_contatos_email2 (email, cpf)


@app.route('/pessoas-deletar', methods=['GET'])
def deletar_pessoas0():
    return render_template('pessoas_deletar.html')


@app.route('/pessoas-deletar', methods=['POST'])
def deletar_pessoas1():
    cpf = request.form['id_cpf_deletar']
    return deletar_pessoas2 (cpf)


@app.route('/contatos-deletar', methods=['GET'])
def deletar_contatos0():
    return render_template('contatos_deletar.html')


@app.route('/contatos-deletar', methods=['POST'])
def deletar_contatos1():
    cpf = request.form['id_cpf_deletar']
    return deletar_contatos2 (cpf)

