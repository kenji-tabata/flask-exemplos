from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "Atd1255d"
app.config['WTF_CSRF_ENABLED'] = False

db = SQLAlchemy(app)

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
# Forms
#
class MyForm(Form):
    # Validação simples
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])

    # Validação personalizada
    def validate(self):
        # Primeiro verifica se todos os campos estão preenchidos
        initial_validation = super(MyForm, self).validate()
        if not initial_validation:
            return False
        # Para depois verificar as validações personalizadas
        if len(self.username.data) < 4:
            self.username.errors.append('Username tem que ser maior que 4 caracteres')
            return False
        return True

#
# Views
#
@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if request.method == "POST" and form.validate_on_submit():
        return "Validado com sucesso"
    else:
        print(form.errors) # {'username': ['This field is required.'], 'email': ['This field is required.']}
    return render_template('submit.html', form=form)

@app.route("/")
def hello_model():
    user = User.query.filter_by(id=1).first()
    return "Hello user %s!" % user.username

#
# Run
#
if __name__ == "__main__":
    app.run(debug=True)