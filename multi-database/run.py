from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Configurações das conexões
app.config['DATABASES'] = {
    'testes': 'sqlite:///test.db',
    'producao': 'sqlite:///prod.db',
    'desenvolvimento': 'sqlite:///dev.db',
}
# Configuração da conexão padrão
app.config['SQLALCHEMY_DATABASE_URI'] = app.config['DATABASES']['testes']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

# Cria uma nova conexão
# http://flask-sqlalchemy.pocoo.org/2.1/api/#flask.ext.sqlalchemy.SQLAlchemy.make_connector
def conectar_db(nome_db):
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['DATABASES'][nome_db]
    db.make_connector(app)


#
# Model
#
class User(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email    = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email    = email

    def __repr__(self):
        return '<User %r>' % self.username


#
# Views
#
@app.route("/")
def hello_model():
    user = User.query.filter_by(id=1).first()
    # http://flask-sqlalchemy.pocoo.org/2.1/api/#flask.ext.sqlalchemy.SQLAlchemy.engine
    print(db.engine)
    return "Hello user %s!" % user.username

@app.route("/<string:nome_db>")
def alterar_db(nome_db):
    conectar_db(nome_db)
    user = User.query.filter_by(id=1).first()
    print(db.engine)
    return "Hello user %s!" % user.username


#
# Run
#
if __name__ == "__main__":
    app.run(debug=True)