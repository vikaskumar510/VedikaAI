from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    return jsonify({'message': 'Welcome to the AI backend!'})

if __name__ == '__main__':
    app.run(debug=True)