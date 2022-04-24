from flask import Flask, request, render_template, jsonify
from db import mysql


def _select_sql(raw_sql):
    cursor = mysql.get_db().connect()
    cursor.execute(raw_sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def consultar_pessoas2():
    autores = _select_sql('SELECT * FROM PYTHON_CRUD_PESSOAS.PESSOAS;')
    return jsonify(autores)


def consultar_contatos2():
    nomes = _select_sql('SELECT * FROM PYTHON_CRUD_PESSOAS.CONTATOS;')
    return jsonify(nomes)


def consultar_pessoas_contatos2():
    SQL_STATEMENT = 'SELECT P.NOME, P.CPF, C.TELEFONE, C.EMAIL '\
        'FROM PYTHON_CRUD_PESSOAS.PESSOAS AS P '\
        'INNER JOIN PYTHON_CRUD_PESSOAS.CONTATOS AS C ON C.ID_PESSOAS = P.ID;'
    nomes = _select_sql(SQL_STATEMENT)
    return jsonify(nomes)
