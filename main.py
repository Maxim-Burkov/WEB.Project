from flask import Flask, render_template, url_for
import flask_login
import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
db = SQLAlchemy(app)

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(300), nullable=False)
    password = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(300), nullable=False)
    surname = db.Column(db.String(300), nullable=False)
    tele = db.Column(db.Text(30), nullable=False)
    email = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        # return '<Post %r>' % self.id
        pass



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(300), nullable=False)
    tele = db.Column(db.Text(30), nullable=False)

    def __repr__(self):
        # return '<Post %r>' % self.id
        pass


@app.route('/')
def index():
    with open('templates/grand.html', 'r', encoding='utf-8') as grand:
        return grand.read()

@app.route('/account')
def account():
    with open('templates/account.html', 'r', encoding='utf-8') as account:
        return account.read()

@app.route('/about')
def about():
    with open('templates/about.html', 'r', encoding='utf-8') as abot:
        return abot.read()


@app.route('/enter')
def enter():
    with open('templates/enter.html', 'r', encoding='utf-8') as go:
        return go.read()


if __name__ == "__main__":
    app.run(debug=True)