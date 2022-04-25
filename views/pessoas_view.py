from flask import render_template, Blueprint, request, jsonify, url_for, redirect

from db import select, insert
# FIXME: deletar dependencias
from atualizar import atualizar_pessoas2
from deletar import deletar_pessoas2

pessoas_view = Blueprint('pessoas', __name__, url_prefix='/pessoas')

@pessoas_view.route('/', methods=['GET', 'POST'])
def cadastrar_pessoas0():
  if request.method == 'GET':
    return render_template('pessoas.html')
  elif request.method == 'POST':
    nome = request.form['id_nome']
    cpf = request.form['id_cpf']
    insert(
      'INSERT INTO PYTHON_CRUD_PESSOAS.PESSOAS (NOME, CPF) VALUES (%s, %s);', (nome, cpf)
    )
    return redirect(url_for('pessoas.consultar_pessoas1'))


@pessoas_view.route('/list', methods=['GET'])
def consultar_pessoas1():
  pessoas = select('SELECT * FROM PYTHON_CRUD_PESSOAS.PESSOAS;')
  return render_template('pessoas_list.html', list=pessoas)


@pessoas_view.route('/contatos-cadastrados', methods=['GET'])
def consultar_pessoas_contatos1():
  SQL_STATEMENT = 'SELECT P.NOME, P.CPF, C.TELEFONE, C.EMAIL '\
      'FROM PYTHON_CRUD_PESSOAS.PESSOAS AS P '\
      'INNER JOIN PYTHON_CRUD_PESSOAS.CONTATOS AS C ON C.ID_PESSOAS = P.ID;'
  nomes = select(SQL_STATEMENT)
  return jsonify(nomes)


@pessoas_view.route('/atualizar', methods=['GET', 'POST'])
def atualizar_pessoas0():
  if request.method == 'GET':
    return render_template('pessoas_atualizar.html')
  elif request.method == 'POST':
    nome = request.form['id_nome_atualizar']
    cpf = request.form['id_cpf_atualizar']
    return atualizar_pessoas2(nome, cpf)


@pessoas_view.route('/deletar', methods=['GET', 'DELETE'])
def deletar_pessoas0():
  if request.method == 'GET':
    return render_template('pessoas_deletar.html')
  elif request.method == 'DELETE':
    cpf = request.form['id_cpf_deletar']
    return deletar_pessoas2 (cpf)
