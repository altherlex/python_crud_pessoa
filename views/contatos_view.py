from flask import render_template, Blueprint, request, jsonify, url_for, redirect

from db import select, insert
# FIXME: deletar dependencias
from atualizar import atualizar_contatos_telefone2, atualizar_contatos_email2
from deletar import deletar_contatos2

contatos_view = Blueprint('contatos', __name__, url_prefix='/contatos')

@contatos_view.route('/', methods=['GET'])
def cadastrar_contatos0():
  if request.method == 'GET':
    return render_template('contatos.html')
  elif request.method == 'POST':
    id_pessoas = request.form['id_pessoas']
    telefone = request.form['id_telefone']
    email = request.form['id_email']
    insert(
        'INSERT INTO PYTHON_CRUD_PESSOAS.CONTATOS (ID_PESSOAS, TELEFONE, EMAIL) VALUES (%s, %s, %s);',
        (id_pessoas, telefone, email)
    )
    return redirect(url_for('contatos.consultar_contatos1'))



@contatos_view.route('/list', methods=['GET'])
def consultar_contatos1():
  contatos = select('SELECT * FROM PYTHON_CRUD_PESSOAS.CONTATOS;')
  # TODO: Create html
  return jsonify(contatos)


@contatos_view.route('/atualizar-telefone', methods=['GET', 'POST'])
def atualizar_contatos_telefone0():
  if request.method == 'GET':
    return render_template('contatos_atualizar_telefone.html')
  elif request.method == 'POST':
    telefone = request.form['id_telefone_atualizar']
    cpf = request.form['id_cpf_atualizar']
    return atualizar_contatos_telefone2(telefone, cpf)


@contatos_view.route('/atualizar-email', methods=['GET', 'POST'])
def atualizar_contatos_email0():
  if request.method == 'GET':
    return render_template('contatos_atualizar_email.html')
  elif request.method == 'POST':
    email = request.form['id_email_atualizar']
    cpf = request.form['id_cpf_atualizar']
    return atualizar_contatos_email2 (email, cpf)


@contatos_view.route('/deletar', methods=['GET', 'DELETE'])
def deletar_contatos0():
  if request.method == 'GET':
    return render_template('contatos_deletar.html')
  elif request.method == 'DELETE':
    cpf = request.form['id_cpf_deletar']
    return deletar_contatos2 (cpf)