from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    with open('templates/grand.html', 'r', encoding='utf-8') as grand:
        return grand.read()

@app.route('/chat')
def chat():
    with open('templates/chat.html', 'r', encoding='utf-8') as chats:
        return chats.read()

@app.route('/account')
def account():
    with open('templates/account.html', 'r', encoding='utf-8') as account:
        return account.read()

@app.route('/about')
def about():
    with open('templates/about.html', 'r', encoding='utf-8') as abot:
        return abot.read()

@app.route('/poisk')
def poisk():
    with open('templates/poisk.html', 'r', encoding='utf-8') as search:
        return search.read()

@app.route('/enter')
def enter():
    with open('templates/enter.html', 'r', encoding='utf-8') as go:
        return go.read()


if __name__ == "__main__":
    app.run(debug=True)