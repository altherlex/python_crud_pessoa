from flask import Flask, request, render_template, jsonify
from db import mysql


def atualizar_pessoas2(nome, cpf):
    if cpf:
         cursor = mysql.get_db().connect()
         cursor.execute(
             f'update python_crud_pessoas.pessoas set nome = "{nome}" where cpf = "{cpf}";'
             )
         conn.commit()
         cursor.close()
         conn.close()
         return render_template('pessoas_atualizar.html')


def atualizar_contatos_telefone2(telefone, cpf):
    if cpf:
         cursor = mysql.get_db().connect()
         cursor.execute(
             f'update python_crud_pessoas.pessoas as p inner join python_crud_pessoas.contatos as c on c.id_pessoas = p.id set c.telefone= "{telefone}" where cpf = "{cpf}";'
             )
         conn.commit()
         cursor.close()
         conn.close()
         return render_template('contatos_atualizar_telefone.html')


def atualizar_contatos_email2(email, cpf):
    if cpf:
         cursor = mysql.get_db().connect()
         cursor.execute(
             f'update python_crud_pessoas.pessoas as p inner join python_crud_pessoas.contatos as c on c.id_pessoas = p.id set c.email= "{email}" where cpf = "{cpf}";'
             )
         conn.commit()
         cursor.close()
         conn.close()
         return render_template('contatos_atualizar_email.html')