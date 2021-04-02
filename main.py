from flask import Flask, render_template, url_for

app = Flask(__name__)

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

@app.route('/regestration')
def regeatration():
    with open('templates/regestration.html', 'r', encoding='utf-8') as reg:
        return reg.read()

@app.route('/enter')
def enter():
    with open('templates/enter.html', 'r', encoding='utf-8') as go:
        return go.read()


if __name__ == "__main__":
    app.run(debug=True)