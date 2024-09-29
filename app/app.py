from flask import Flask, jsonify

app = Flask(__name__)

# Define the /api/helloworld endpoint
@app.route('/api/helloworld', methods=['GET'])
def hello_world():
    return jsonify(message="Hello World")

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

