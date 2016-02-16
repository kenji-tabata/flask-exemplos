from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from forms import MyForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "Atd1255d"
app.config['WTF_CSRF_ENABLED'] = False

db = SQLAlchemy(app)
class User(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email    = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email    = email

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return "Validado com sucesso"
    else:
        print(form.errors) # {'username': ['This field is required.'], 'email': ['This field is required.']}
    return render_template('submit.html', form=form)

@app.route("/")
def hello_model():
    user = User.query.filter_by(id=1).first()
    return "Hello user %s!" % user.username

if __name__ == "__main__":
    app.run(debug=True)