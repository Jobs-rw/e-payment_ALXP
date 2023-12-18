#!/usr/bin/python3
from flask import Flask, render_template, request, redirect, url_for
from Models.engine.db_manager import Database
from Models.engine.user_manager import UserManager
from Models.user import User
from datetime import datetime, timedelta
from Models.customers import Customer
from werkzeug.exceptions import BadRequest
import os
from Models.GPS import GPSTracker

app = Flask(__name__)


# Retrieve database credentials from environment variables
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'jobs123', 
    'database': 'e_payment' 
}

db = Database(db_config)

@app.route('/')
def index():
    """The default page."""
    return redirect(url_for('login'))

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
        # Check for the existence of required form fields
        if all(field in request.form for field in ['first_name', 'last_name', 'email']):
            # Access form data
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            create_date = datetime.now()
            last_update = datetime.now()
            active = 'active' in request.form

            # Create a Customer object with the form data
            customer = Customer(
                first_name=first_name,
                last_name=last_name,
                email=email,
                active=active,
            )

            # Add the customer to the database
            registration_result = db.Add_customer(customer)
            print(registration_result)

            # Redirect after successful form submission
            return render_template('success_template.html', redirect_url=url_for('add_customer'))
            #return f"The new customer has been saved"
        else:
            # Handle the case when required form fields are missing
            flash('Please fill out all required fields.')
            return redirect(url_for('add_customer'))
    else:
        return render_template('add_customer.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        user_manager = UserManager(db_config)
        print(username)
        print(password)
        login_result, user_data = user_manager.login_user(username, password)
        print(login_result)

        if login_result == "Login successful!":
            # Authentication successful, redirect to a new page or perform further actions
            return render_template('welcome.html', user={'username': username})
        else:
            # Authentication failed, redirect back to the login page with a message
            return render_template('login.html', message='Invalid credentials. Please try again.')
    else:
        # Handle the case where 'username' or 'password' is not present in the form data
        return render_template('login.html', message='Invalid form data. Please try again.')


@app.route('/register_tracker', methods=['GET', 'POST'])
def register_tracker():
    if request.method == 'POST':
        EMEI = request.form['EMEI']
        Model_Name = request.form['Model_Name']
        Activated_date = datetime.strptime(request.form['Activated_date'], '%Y-%m-%d')
        GPS_Experied_date = datetime.strptime(request.form['GPS_Experied_date'], '%Y-%m-%d')

        new_tracker = GPSTracker(
            EMEI=EMEI,
            Model_Name=Model_Name,
            Activated_date=Activated_date,
            GPS_Experied_date=GPS_Experied_date
        )
        registration_result = db.Add_GPS(new_tracker)
        return redirect(url_for('tracker_registered', EMEI=int(EMEI)))

    return render_template('register_tracker.html')

@app.route('/tracker_registered/<int:EMEI>')
def tracker_registered(EMEI):
    query = 'SELECT * FROM gps WHERE EMEI = %s'
    tracker = db.fetch_one(query, (EMEI,))
    print(tracker)
    return render_template('tracker_registered.html', tracker=tracker)

@app.route('/search_emei', methods=['GET', 'POST'])
def search_emei():
    """Search for the emei based on user input."""
    if request.method == 'POST':
        EMEI = request.form['EMEI']
        query = 'SELECT * FROM gps WHERE EMEI = %s'
        tracker = db.fetch_one(query, (EMEI,))
        print(tracker)
        return f'EMEI: {tracker[0]} Model: {tracker[1]} Created at: {tracker[2]}, \nsee you next time.'
    return render_template('search_emei.html')



if __name__ == '__main__':
    app.run( host='0.0.0.0', port='4500', debug=True)
