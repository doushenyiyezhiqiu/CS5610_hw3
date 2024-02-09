from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

# Configure your database connection here
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="scb78377837",
  database="mybloglogin"
)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']

    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usernameandpassword WHERE username = %s", (username,))
    user = cursor.fetchone()

    # if user and check_password_hash(user['password'], password):
    if user and user['password'] == password:
        # Login success
        return jsonify({"success": True, "message": "Login successful"})
    else:
        # Login failed
        return jsonify({"success": False, "message": "Invalid credentials"}), 401

@app.route('/login', methods=['GET'])
def showMessage():
    return "Test app successful!!!"

if __name__ == '__main__':
    app.run(debug=True)
