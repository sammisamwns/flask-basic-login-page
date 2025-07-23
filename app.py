from flask import Flask, request, jsonify
from flask_cors import CORS
import jwt
import datetime

app = Flask(__name__)
CORS(app)

# Secret key to encode and decode JWT
app.config['SECRET_KEY'] = 'your_secret_key_here'

# In-memory user (replace with DB in real app)
users = {'admin': 'password123'}

# In-memory token blacklist
blacklist = set()

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if users.get(username) == password:
        token = jwt.encode({
            'user': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'token': token,"message":"Login successful"})
    else:
        return jsonify({'error': 'Invalid credentials',"message":"Login failed"}), 401

@app.route('/logout', methods=['POST'])
def logout():
    token = request.headers.get('Authorization')
    if token:
        blacklist.add(token)
        return jsonify({'message': 'Logged out successfully'})
    return jsonify({'error': 'Token required',"message":"Token required"}), 400

@app.route('/protected', methods=['GET'])
def protected():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'error': 'Token missing'}), 403
    if token in blacklist:
        return jsonify({'error': 'Token is blacklisted'}), 401

    try:
        decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return jsonify({'message': f'Hello, {decoded["user"]}!'} )
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Invalid token'}), 401

if __name__ == '__main__':
    app.run(debug=True, port=5000) 