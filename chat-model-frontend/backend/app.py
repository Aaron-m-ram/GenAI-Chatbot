from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message')

    bot_response = f"Bot received: {user_message}"

    return jsonify({'response': bot_response})


if __name__ == '__main__':
    app.run(port=5000, debug=True)
