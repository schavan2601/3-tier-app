from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# Database path
DB_PATH = "/data/user_data.db"

@app.route('/users', methods=['GET'])
def get_users():
    """Fetch all users from the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()

    # Convert to JSON
    user_list = []
    for user in users:
        user_list.append({
            'id': user[0],
            'name': user[1],
            'email': user[2],
            'age': user[3]
        })

    return jsonify(user_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)