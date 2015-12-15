Manipulando os dados no terminal
===

### Criando e removendo base de dados

```python
from yourapplication import db
db.create_all()
db.drop_all()
```


### Adicionando usuários

```python
from yourapplication import User

admin = User('admin', 'admin@mail.com')
guest = User('guest', 'guest@mail.com')
db.session.add(admin)
db.session.add(guest)
db.session.commit()
```


### Exibindo lista de usuários

```python
from yourapplication import User

User.query.all()
```


### Exibindo um usuário

```python
from yourapplication import User

User.query.filter_by(login='admin').first()
User.query.filter_by(login='admin').first().nome
```


### Adicionando modelos com relação de um para muitos

Uma categoria tem vários posts.

```python
from yourapplication import User
from yourapplication import Category
from yourapplication import Post

py = Category('Python')
db.session.add(py)

admin = User.query.filter_by(login='admin').first()
p = Post('Hello Python', 'Python is pretty cool', py, admin)
db.session.add(p)

guest = User.query.filter_by(login='guest').first()
pp = Post('Training with Python', 'Python code', py, guest)
db.session.add(pp)

db.session.commit()
```


### Visualizando todos os posts 

from yourapplication import Post
Post.query.all()


### Visualizando todos os posts de um usuário

from yourapplication import User
u = User.query.filter_by(login='admin').first()
u.posts.all()


### Visualizando todos os posts de uma categoria

from yourapplication import Category
c = Category.query.filter_by(id=1).first()
c.posts.all()

