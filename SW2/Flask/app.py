from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/reverse', methods=['POST'])
def reverse_text():
    data = request.get_json()
    text = data.get('text', '')
    reversed_text = text[::-1]
    return jsonify({'reversed': reversed_text})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Für Azure Deployment wichtig
    app.run(host='0.0.0.0', port=port)