import random
from flask import Flask, jsonify, render_template

app = Flask(__name__)

words = ['python', 'hangman', 'challenge', 'programming', 'developer']

@app.route('/words', methods=['GET'])
def get_words():
    return jsonify(words)

@app.route('/random_word', methods=['GET'])
def get_random_word():
    return jsonify(random.choice(words))

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
