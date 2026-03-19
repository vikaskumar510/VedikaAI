from flask import Flask, jsonify
import random

app = Flask(__name__)

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the coffee file a police report? It got mugged!",
    "What do you call fake spaghetti? An impasta!",
    "Why was the math book sad? Because it had too many problems!",
]

@app.route('/joke', methods=['GET'])
def random_joke():
    joke = random.choice(jokes)
    return jsonify({'joke': joke})

if __name__ == '__main__':
    app.run(debug=True)