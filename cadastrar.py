from flask import Flask, request, render_template, jsonify
from db import mysql


def cadastrar_pessoas2(nome, cpf):
    conn = mysql.connect()
    cursor = conn.cursor()
    # cursor = mysql.get_db().connect()
    cursor.execute(
        'INSERT INTO PYTHON_CRUD_PESSOAS.PESSOAS (NOME, CPF) VALUES (%s, %s);', 
        (nome, cpf)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return render_template('pessoas.html')


def cadastrar_contatos2(id_pessoas, telefone, email):
    cursor = mysql.get_db().connect()
    cursor.execute(
        'INSERT INTO PYTHON_CRUD_PESSOAS.CONTATOS (ID_PESSOAS, TELEFONE, EMAIL) VALUES (%s, %s, %s);', 
        (id_pessoas, telefone, email)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return render_template('contatos.html')