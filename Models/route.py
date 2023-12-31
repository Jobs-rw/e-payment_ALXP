#!/usr/bin/python3
from flask import Flask, render_template, request, redirect, url_for
from engine.db_manager import Database
from engine.user_manager import UserManager
from user import User
app = Flask(__name__)


db_config = {
        'host' : 'localhost',
        'user' : 'root',
        'password' : 'jobs123',
        'database' : 'e_payment'
}

db = Database(db_config)

@app.route('/insert_user', methods=['POST', 'GET'])
def insert_user():
    """Insert User in the database."""
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        role = request.form['role']
        phone = request.form['phone']

        print(f'phone:{phone}')
        print(f'role: {role}')
        print(username)
        print(password)
        print(email)
        print(first_name)
        print(last_name)

        print(request.form)

        user = User(email=email, username=username, password=password, role=role, first_name=first_name, last_name=last_name, phone=phone)
        registration_result = db.insert_user(user)
        return render_template('registration_success.html')
    else:
        return render_template('register.html')



@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    user_manager = UserManager(db_config)
    login_result, user_data = user_manager.login_user(username, password)

    if login_result == "Login successful!":

        # Authentication successful, redirect to a new page or perform further actions
        return f"Welcome, {username}!"
    else:
        # Authentication failed, redirect back to the login page with a message
        return render_template('login.html', message='Invalid credentials. Please try again.')

if __name__ == '__main__':
    app.run( host='0.0.0.0', port='4500', debug=True)
