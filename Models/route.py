from flask import Flask, render_template, request, redirect, url_for
<<<<<<< HEAD
from Models.engine.db_manager import Database
=======
>>>>>>> f0e3c232cbd21334ba73fc94f9e388400327a73f
app = Flask(__name__)

users = {
    'user': 'root',
    'password': 'jobs123',
    'host': 'localhost',
    'database': 'e-payment',
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in users and users[username] == password:
        # Authentication successful, redirect to a new page or perform further actions
        return f"Welcome, {username}!"
    else:
        # Authentication failed, redirect back to the login page with a message
        return render_template('login.html', message='Invalid credentials. Please try again.')

if __name__ == '__main__':
    app.run( host='0.0.0.0', debug=True)
