Flask-migrate
===

Por padrão o Flask-SqlAlchemy não possui um comando para alterar ou adicionar colunas em tabelas 
que já foram criadas com o comando db.create_all(). É possível adicionar manualmente pelo PyMsyql ou 
adicionando automaticamente como no Django com o módulo Flask-migrate.

Para instalar digite...

    pip install flask-migrate


Após a instalação adicione no model as seguintes linhas...

```python
#
# Conteúdo do arquivo "yourapplication.py"
#
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# imports do flask-migrate
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)

# parâmetros do flask-migrate
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

# o parâmetro de execução flask-migrate sempre deve ficar no final do arquivo
if __name__ == '__main__':
    manager.run()
```

Para iniciar o migrate na pasta da aplicação digite no terminal...

    $ python app.py db init


Verifique se há alterações...

    $ python app.py db migrate


E execute as alterações se houver...

    $ python app.py db upgrade


Para ajuda e demais comandos...

    $ python app.py db --help


O Flask-migrate possui integração com multiple database binds do SqlAlchemy. Utilize o comando abaixo 
para inicializar com as associações do multi-db.

    $ python app.py db init --multidb

[Documentação](https://flask-migrate.readthedocs.org/en/latest/)