#!/usr/bin/python3
from flask import Flask, render_template, request, redirect, url_for
from engine.db_manager import Database
from engine.user_manager import UserManager
from user import User
from customers import Customer
import os

app = Flask(__name__)


# Retrieve database credentials from environment variables
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'jobs123', 
    'database': 'e_payment' 
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
@app.route('/add_customer', methods=['POST', 'GET'])
def add_customer():
    if request.method == 'POST':
        # Access form data directly without unnecessary conversion functions
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']
        active = request.form['active']
        create_date = request.form['create_date']
        last_update = request.form['last_update']

        # Create a Customer object with the form data
        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            active=active,
            create_date=create_date,
            last_update=last_update
        )

        # Add the customer to the database
        registration_result = db.add_customer(customer)

        # Redirect after successful form submission
        return redirect(url_for('registration_success'))

    else:
        return render_template('add_customer.html')


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    username = request.form['username']
    password = request.form['password']
    user_manager = UserManager(db_config)
    print(username)
    print(password)
    login_result, user_data = user_manager.login_user(username, password)

    if login_result == "Login successful!":

        # Authentication successful, redirect to a new page or perform further actions
        return f"Welcome, {username}!"
    else:
        # Authentication failed, redirect back to the login page with a message
        return render_template('login.html', message='Invalid credentials. Please try again.')

if __name__ == '__main__':
    app.run( host='0.0.0.0', port='4500', debug=True)
