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
        return jsonify({"success": False, "message": "Invalid credentials"})


@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data['username']
    password = data['password']

    # Optional: Hash the password for security
    # password_hash = generate_password_hash(password)

    cursor = db.cursor(dictionary=True)

    # Check if username already exists
    cursor.execute("SELECT * FROM usernameandpassword WHERE username = %s", (username,))
    if cursor.fetchone():
        return jsonify({"success": False, "message": "Username already exists"})

    # Insert new user into the database
    try:
        cursor.execute("INSERT INTO usernameandpassword (username, password) VALUES (%s, %s)", (username, password))
        db.commit()
        return jsonify({"success": True, "message": "User registered successfully"})
    except mysql.connector.Error as err:
        return jsonify({"success": False, "message": str(err)})

@app.route('/delete_account', methods=['POST'])
def delete_account():
    data = request.json
    username = data['username']

    cursor = db.cursor(dictionary=True)
    cursor.execute("DELETE FROM usernameandpassword WHERE username = %s", (username,))
    db.commit()

    if cursor.rowcount > 0:
        return jsonify({"success": True, "message": "Account deleted successfully"})
    else:
        return jsonify({"success": False, "message": "Account not found"})

@app.route('/post_message', methods=['POST'])
def post_message():
    data = request.json
    message = data['message']

    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO welcome_messages (message) VALUES (%s)", (message,))
        db.commit()
        return jsonify({"success": True, "message": "Message posted successfully"})
    except Exception as e:
        db.rollback()
        return jsonify({"success": False, "message": str(e)}), 500

@app.route('/get_messages', methods=['GET'])
def get_messages():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT message FROM welcome_messages ORDER BY created_at DESC")
    messages = cursor.fetchall()
    return jsonify(messages)

@app.route('/login', methods=['GET'])
def showMessage():
    return "Test app successful!!!"

if __name__ == '__main__':
    app.run(debug=True)
