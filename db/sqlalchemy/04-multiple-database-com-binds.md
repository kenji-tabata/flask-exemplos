Multiple Databases com Binds
===

Com o parâmetro `SQLALCHEMY_BINDS` podemos definir quais modelos serão criados fora da base de dados padrão 
da aplicação.

Adicione o parâmetro `SQLALCHEMY_BINDS` abaixo do `SQLALCHEMY_DATABASE_URI` e configure as conexões adicionais 
com o login, senha e nome da base de dados.

```python
#
# Conteúdo do arquivo "yourapplication.py"
#
SQLALCHEMY_DATABASE_URI = 'postgres://localhost/main'
SQLALCHEMY_BINDS = {
    'users':        'mysqldb://localhost/users',
    'appmeta':      'sqlite:////path/to/appmeta.db'
}
```

E adicione o atributo `__bind_key__` no model que será armazenada em outra base de dados.

```python
#
# Conteúdo do arquivo "yourapplication.py"
#
class User(db.Model):
    __bind_key__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
```

Se o `__bind_key__` não for definido no model todas as tabelas serão criadas na base de dados padrão.

No terminal podemos...

```python
$ python
>>> from yourapplication import db

# Criar todas as tabelas

>>> db.create_all()

# Criar apenas uma tabela especifica

>>> db.create_all(bind='users')

# Criar apenas as tabelas listadas

>>> db.create_all(bind=['users', 'appmeta'])

# Criar apenas as tabelas que não possuem o parâmetro `__bind_key__`

>>> db.create_all(bind=None)
```

O parâmetro `bind` funciona da mesma forma tanto na função create_all() como na drop_all().

[Documentação](http://flask-sqlalchemy.pocoo.org/1.0/binds/)