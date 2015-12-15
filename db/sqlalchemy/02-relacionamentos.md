Relacionamentos
===

Relacionamento simples
---

Adicionando uma referencia entre Post e Category. 
Adicione o conteúdo abaixo em sua aplicação, considere em adicionar na mesma aplicação anterior.

```python
#
# Conteúdo do arquivo "yourapplication.py"
#
from datetime import datetime

class Post(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    title    = db.Column(db.String(80))
    body     = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)
        
    # Referencia para a Category
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category    = db.relationship('Category',
        backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, title, body, category, pub_date=None):
        self.title    = title
        self.body     = body
        if pub_date is None:
            pub_date  = datetime.utcnow()
        self.pub_date = pub_date
        self.category = category

    def __repr__(self):
        return '<Post %r>' % self.title

class Category(db.Model):
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name

```

Agora no terminal importamos as aplicações e instanciamos uma Category e 
alguns Posts. 

```python
$ python
>>> from yourapplication import db
>>> from yourapplication import Category
>>> from yourapplication import Post

### Instanciando Category e Posts

>>> py = Category('Python')
>>> p1 = Post('Hello Python', 'Python is pretty cool', py)
>>> p2 = Post('Training with Python', 'Python code', py)

### Create

>>> db.session.add(py)
>>> db.session.add(p1)
>>> db.session.add(p2)
>>> db.session.commit()
```

### Read

```python
>>> Post.query.all()
'[<Post 'Hello Python'>, <Post 'Training with Python'>'

>>> c = Category.query.get(1)
>>> c.posts.all()
'[<Post 'Hello Python'>, <Post 'Training with Python'>]'
```


One-to_many
---

Outra forma para adicionarmos um relacionamento de um para muitos é atribuindo o campo com `db.relationship` 
separado do campo com `foreignKey`, desta forma fica visível o relacionamento de um para muitos em ambos os 
models.

```python
class Person(db.Model):
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    addresses = db.relationship('Address', backref='person',
                                lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Person %r>' % self.name

class Address(db.Model):
    id        = db.Column(db.Integer, primary_key=True)
    email     = db.Column(db.String(50))
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    
    def __init__(self, email, person):
        self.email = email
        self.person = person

    def __repr__(self):
        return '<Address %r>' % self.email
```

Podemos adicionar um Person sem ter o Address cadastrado uma vez que o campo address do Person é 
uma referencia.

```python
$ python
>>> from yourapplication import db
>>> from yourapplication import Person
>>> from yourapplication import Address

### Instanciando Person e Address

>>> p = Person('Maria')
>>> a = Address('maria@mail.com', p)

### Create

>>> db.session.add(p)
>>> db.session.add(a)
>>> db.session.commit()
```


One-to-One
===

Para relacionamentos um-para-um colocamos o parâmetro `uselist=False` no campo que possui o `db.relationship`, 
desta forma o model que possui a `foreignKey` sempre será modificado ao atribui um novo valor.

```
class Image(db.Model):
    id       = db.Column(db.Integer, primary_key = True)
    name     = db.Column(db.String(8))
    blindmap = db.relationship("Blindmap", uselist=False,
        backref='image')
        
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Image %r>' % self.name

class Blindmap(db.Model):
    id       = db.Column(db.Integer, primary_key = True)
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'))
```

Ao inserir uma Image...

```python
$ python
>>> from yourapplication import db
>>> from yourapplication import Image
>>> from yourapplication import Blindmap
>>> i = Image('jpg')
>>> b = Blindmap()
>>> b.image=i

### Create

>>> db.session.add(i)
>>> db.session.add(b)
>>> db.session.commit()


Many-to-Many
===

Define uma tabela de ajuda que fará a conexão entre os dois models. O parâmetro `tags` do model Page 
referencia o id do model Tag.

```python
tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('page_id', db.Integer, db.ForeignKey('page.id'))
)

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    tags = db.relationship('Tag', secondary=tags,
        backref=db.backref('pages', lazy='dynamic'))

    def __init__(self, title, tags):
        self.title = title
        self.tags = tags

    def __repr__(self):
        return '<Page %r>' % self.title

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Tag %r>' % self.name
```


Para inserirmos as Pages com a Tag...

```python
$ python
>>> from yourapplication import db
>>> from yourapplication import Page
>>> from yourapplication import Tag

>>> t = Tag('Flask')
>>> p = Page('Tutorial Flask', [t])


### Create

db.session.add(p)
db.session.commit()


### Read

Recuperando as tags de cada posts

>>> a=Page.query.filter_by(1)
>>> a
<Page 'Tutorial Flask'>
>>> a.tags
[<Tag 'Flask'>]
```

[Documentação](http://flask-sqlalchemy.pocoo.org/1.0/models/)
[Exemplo completo do One-to-One](http://stackoverflow.com/a/24934509)
[Exemplo completo do Many-to-Many](http://librelist.com/browser/flask/2011/11/12/sqlalchemy-add-method-for-many-to-many-relationship/#068423c8092c2154ccfe08268711ec03)
