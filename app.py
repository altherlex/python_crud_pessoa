import os
from flask import Flask, render_template

from settings import APP_FOLDER
from views.contatos_view import contatos_view
from views.pessoas_view import pessoas_view
from db import mysql

app = Flask(__name__)
app.config.from_pyfile(os.path.join(APP_FOLDER, "settings.py"))
mysql.init_app(app)

app.register_blueprint(contatos_view)
app.register_blueprint(pessoas_view)

@app.route('/index', methods=['GET'])
@app.route('/', methods=['GET'])
def index():
  return render_template('main.html', title='CP - Main')
