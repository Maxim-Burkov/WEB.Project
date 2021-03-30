from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/poisk')
def poisk():
    return render_template('poisk.html')

@app.route('/enter')
def enter():
    return render_template('enter.html')


if __name__ == "__main__":
    app.run(debug=True)