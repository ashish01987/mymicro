from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configuring the database (using SQLite for simplicity)
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///messages.db')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define a simple Message model
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)

# Function to create tables and seed the database
def initialize_database():
    with app.app_context():
        db.create_all()
        if not Message.query.first():
            # Seed the database with an initial "Hello World" message if empty
            hello_world_message = Message(text="Hello World")
            db.session.add(hello_world_message)
            db.session.commit()

# API to fetch the message
@app.route('/api/message', methods=['GET'])
def get_message():
    message = Message.query.first()  # Fetch the first message from the database
    if message:
        return jsonify({"message": message.text})
    else:
        return jsonify({"error": "No message found"}), 404

if __name__ == '__main__':
    # Initialize the database and seed data when the app starts
    initialize_database()
    app.run(host='0.0.0.0', port=5001)

