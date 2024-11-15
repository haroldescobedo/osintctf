from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Welcome to CTF!"

if __name__ == '__main__':
    app.run(debug=True)