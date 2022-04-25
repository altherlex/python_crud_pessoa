from flask import Flask, request, render_template, jsonify
# from db import mysql
from flask import g



def deletar_pessoas2(cpf):
    if cpf:
        cursor = mysql.get_db().connect()
        cursor.execute(
            f'delete from python_crud_pessoas.pessoas where cpf = "{cpf}";'
        )
        conn.commit()
        cursor.close()
        conn.close()
        return render_template('pessoas_deletar.html')


def deletar_contatos2(cpf):
    if cpf:
        cursor = mysql.get_db().connect()
        cursor.execute(
            f'delete c from python_crud_pessoas.pessoas as p inner join python_crud_pessoas.contatos as c on c.id_pessoas = p.id where cpf = "{cpf}";'
        )
        conn.commit()
        cursor.close()
        conn.close()
        return render_template('contatos_deletar.html')