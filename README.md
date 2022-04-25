# Projeto: Python CRUD - Cadastro de Pessoas

*Objetivo:* Criar uma aplicação Full Stack (Front-End + Back-End) que faça uma operação completa de CRUD (Create, Read, Update, Delete).
*Como Funciona:* Ao acessar a aplicação, o usuário se depara com uma página inicial com Menu para cadastrar, atualizar, deletar ou consultar cadastro de pessoas ou contatos. Ao clicar em uma das opções, o usuário é direcionado para página com campos que devem ser preenchidos de acordo com a escolha.

### Comandos Uteis

```
mysql> source /Users/altheralves/dev/desenv/python_crud_pessoa/database.sql
$ pip install -r requirements.txt
$ python run.py
```

### Stack:

- Python
- Flask
- Jinja Template engine
- MySQL
- Flask-MySQL
- Bootstrap

### Aprenda Mais

- [Flask Quickstart](https://flask.palletsprojects.com/en/2.1.x/quickstart/)
- [Jinja](https://flask.palletsprojects.com/en/2.1.x/templating/) - Flask default engine template
- [Bootstrap](https://getbootstrap.com/) - Front-end toolkit

### Outros Flask Apps

* https://github.com/shuhaowu/projecto
* https://github.com/olawalejarvis/blog_api_tutorial
* https://github.com/thefurorjuror/VRS

## TODO

- Flask/Jinja template broken - base.html should render main.html
- Criar Model Sobre
- <strike>Reorganizar app em views com Blueprint</strike>
- Deploy Heroku