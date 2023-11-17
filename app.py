# simple_api.py
from flask import Flask, jsonify
from trends import get_trending_repos

app = Flask(__name__)

@app.route('/')
@app.route('/daily', methods=['GET'])
def home():
    return jsonify(get_trending_repos())

if __name__ == '__main__':
    app.run(debug=True)