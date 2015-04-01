SQLAlchemy
===

Para utilizar o [SQLAlchemy](https://pythonhosted.org/Flask-SQLAlchemy/)
você precisa tê-lo instalado em seu projeto.

    pip install slqalchemy

Além disso, dependendo de sua escolha como bando de dados, você deve ter o driver
de seu banco tamém devidamente instalado.

Para usuários do MySQL você terá duas opções de divers: MySQLdb e pymysql.

Crie um arquivo denominado `yourapplication.py` com o seguinte conteúdo...

```python
#
# Conteúdo do arquivo "yourapplication.py"
#

# coding: utf-8
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "veja opções adiante"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username
```


O valor de `SQLALCHEMY_DATABASE_URI` irá depender de seu banco de dados.

1. sqlite: 

    "sqlite:////tmp/test.db"

2. MySQL com dirver MySQLdb:

    "mysql://user:password@localhost/name-database"

3. MySQL com dirver pymysql:

    "mysql+pymysql://user:password@localhost/name-database"

4. PostgreSQL:

    "postgresql://user:password@localhost/name-database"


Definido o banco de dados, acione o Python pelo terminal.

Obviamente, o Python deve ser acionado estando-se na mesma pasta onde criamos o
arquivo `yourapplication.py`.

    $ ls
    yourapplication.py    
    $ Python

Crie a base de dados e gere o "schema" executando `create_all()`.

    >>> from yourapplication import db
    >>> db.create_all()

Vamos instanciar alguns usuários.

    >>> from yourapplication import User
    >>> admin = User('admin', 'admin@example.com')
    >>> guest = User('guest', 'guest@example.com')

Vamos salvá-los.

    >>> db.session.add(admin)
    >>> db.session.add(guest)
    >>> db.session.commit()

Recupre as informaçẽos do banco.

    >>> users = User.query.all()
    >>> for user in users:
    >>>   user.username
    ...
    admin
    guest

