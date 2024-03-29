#!/usr/bin/python3
from flask import Flask, render_template, request, redirect, url_for, flash
from Models.engine.db_manager import Database
from Models.engine.user_manager import UserManager
from Models.user import User
from Models.payment import Payment
from datetime import datetime, timedelta
from Models.customers import Customer
from werkzeug.exceptions import BadRequest
import os
from Models.GPS import GPSTracker
from Models.moto import Moto

app = Flask(__name__)
app.secret_key = 'Jobs777'

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
@app.route('/update_user/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    user = db.get_user_by_id(user_id)

    if request.method != 'POST':
        try:
            # Validate form data
            validate_user_form(request.form)

            # Update user information in the database
            # Retrieve form data and update the user object
            user.first_name = request.form['first_name']
            user.last_name = request.form['last_name']
            user.email = request.form['email']
            user.username = request.form['username']
            user.role = request.form['role']
            user.phone = request.form['phone']

            """ Perform the update in the database"""
            db.update_user(user)

            # Flash a success message
            flash('User information updated successfully!', 'success')

            # Redirect to the updated user profile
            return render_template('update_user.html', user=user)

            #return redirect(url_for('user_profile', user_id=user.id))

        except ValidationError as e:
            # Flash an error message
            flash(str(e), 'error')

    #return render_template('update_user.html', user=user)
    return redirect(url_for('user_profile', user_id=user.id))

@app.route('/user_information', methods=['GET'])
def user_information():
    """this method help us to retrieve user information"""
    db = Database(db_config)
    user_data = db.get_user_data(db.db_connection)
    db.close_connection()
    return render_template('user_information_template.html', users=user_data)

@app.route('/user_profile/<int:user_id>')
def user_profile(user_id):
    """"Fetch user data from the database based on user_id"""
    user = get_user_by_id(user_id)

    if user:
        return render_template('user_profile.html', user=user)
    else:
        return render_template('user_not_found.html')

@app.route('/add_customer', methods=['POST', 'GET'])
def add_customer():
    gps_records = None

    if request.method == 'POST':
        # Handle the POST request
        if all(field in request.form for field in ['first_name', 'last_name', 'email']):
            # Access form data
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            create_date = datetime.now()
            last_update = datetime.now()
            active = 'active' in request.form
            gps_id = request.form.get('gps_id')
            #gps_id = db.get_gps_id_by_EMEI(EMEI)
            gps_records = db.get_all_gps_records()
            print(gps_records)

            """ Create a Customer object with the form data"""
            customer = Customer(
                first_name=first_name,
                last_name=last_name,
                email=email,
                active=active,
                gps_id=gps_id
            )

            # Add the customer to the database
            registration_result = db.Add_customer(customer)
            print(registration_result)

            # Redirect after successful form submission
            return render_template('success_template.html', redirect_url=url_for('add_customer'), gps_records=gps_records)
        else:
            # Handle the case when required form fields are missing
            flash('Please fill out all required fields.')
            return redirect(url_for('add_customer'))
    else:
        # Handle the GET request
        gps_records = db.get_all_gps_records()

        if gps_records is not None:
            return render_template('add_customer.html', available_gps_records=gps_records)
        else:
            flash('Failed to retrieve GPS records. Please try again later.')
            return redirect(url_for('add_customer'))

@app.route('/update_customer/<int:customer_id>', methods=['GET', 'POST'])
def update_customer(customer_id):
    if request.method == 'POST':
        if all(field in request.form for field in ['first_name', 'last_name', 'email']):
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            active = 'active' in request.form
            update_result = db.update_customer(customer_id, first_name, last_name, email, active)
            
            if update_result:
                flash('Customer information updated successfully.', 'success')
                return redirect(url_for('customer_profile', customer_id=customer_id))
            else:
                flash('Error updating customer information. Please try again.', 'error')
                return redirect(url_for('update_customer', customer_id=customer_id))
        else:
            """Handle the case when required form fields are missing"""
            flash('Please fill out all required fields.', 'error')
            return redirect(url_for('update_customer', customer_id=customer_id))
    else:
        """ Fetch existing customer data for pre-filling the form"""
        customer = db.get_customer_by_id(customer_id)
        if customer:
            return render_template('update_customer.html', customer=customer)
        else:
            flash('Customer not found.', 'error')
            return redirect(url_for('customer_list'))

@app.route('/customer_information', methods=['GET'])
def customer_information():
    """this method will retrieve all customers on template"""
    db = Database(db_config)
    customers = db.get_all_customers()
    db.close_connection()
    return render_template('customer_information_template.html', customers=customers)

@app.route('/welcome', methods=['POST', 'GET'])
def welcome():
    return render_template('dashboard.html')

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
            return render_template('dashboard.html', user={'username': username})
        else:
            # Authentication failed, redirect back to the login page with a message
            return render_template('login.html', message='Invalid credentials. Please try again.')
    else:
        # Handle the case where 'username' or 'password' is not present in the form data
        return render_template('login.html', message='Invalid form data. Please try again.')
@app.route('/insert_payment', methods=['POST','GET'])
def insert_payment():
    if request.method == 'POST':
        # Retrieve form data
        customer_id = request.form['customer_id']
        amount_paid_str = request.form['amount_paid']
        
        # Check if customer_id and amount_paid are empty
        if not customer_id.strip():
            flash('Customer ID cannot be empty.', 'error')
            return redirect(url_for('insert_payment'))
        if not amount_paid_str.strip():
            flash('Amount paid cannot be empty.', 'error')
            return redirect(url_for('insert_payment'))

        try:
            amount_paid = float(amount_paid_str)
        except ValueError:
            flash('Invalid amount paid value.', 'error')
            return redirect(url_for('insert_payment'))

        # Calculate daily credit
        daily_credit = 300  # Adjust this value if needed
        create_date = db.get_customer_create_date(customer_id)
        if create_date:
            days_since_creation = (datetime.now().date() - create_date.date()).days
            daily_balance_increase = daily_credit * days_since_creation
        else:
            daily_balance_increase = 0
        # Create a Payment object with form data
        payment = Payment( customer_id, amount_paid)
        db.insert_payment(payment)

        # Retrieve previous balance and over_credit for the customer
        previous_balance = db.get_previous_balance(customer_id)
        previous_over_credit = db.get_previous_over_credit(customer_id)

        # Perform the rest of the payment insertion logic here
        # (Calculate new balance, over_credit, and insert payment into the database)

        # Example of performing the payment insertion logic
        # Calculate the new balance
        new_balance = previous_balance + daily_balance_increase - amount_paid
        # Ensure new_balance and over_credit are non-negative
        if new_balance < 0:
            over_credit = max(-new_balance, previous_over_credit)
            new_balance = max(0, previous_over_credit - over_credit)
        else:
            over_credit = 0

        # Insert payment into the database
        if db.insert_payment(payment):
            # Redirect to a success page or home page
            flash('Payment inserted successfully', 'success')
            print("ppayment ", payment)
            return redirect(url_for('insert_payment'))
        else:
            # Handle insertion failure
            flash('Failed to insert payment', 'error')
            return redirect(url_for('insert_payment'))

    # Render the form template
    return render_template('insert_payment.html')


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

@app.route('/gps_information', methods=['GET'])
def gps_information():
    """ Database class with a method get_gps_data"""
    gps_data = db.get_gps_data(db.db_connection)

    if gps_data is None:
        """ Handle the case where data retrieval failed"""
        flash("Failed to retrieve GPS data", "error")
        return render_template('gps_information_template.html', gps_data=[])

    return render_template('gps_information_template.html', gps_data=gps_data)

@app.route('/add_moto', methods=['GET', 'POST'])
def add_moto():
    if request.method == 'POST':
        """Handle the POST request for adding a moto"""
        plate = request.form.get('plate')
        Model = request.form.get('Model')
        Chassis_Number = request.form.get('Chassis_Number')
        Engine_Number = request.form.get('Engine_Number')

        """ Retrieve the selected GPS ID from the form"""
        gps_id = request.form.get('gps_id')

        """ Create a Moto object with the form data """
        moto = Moto(
            plate=plate,
            Model=Model,
            Chassis_Number=Chassis_Number,
            Engine_Number=Engine_Number,
            gps_id=gps_id
        )

        """ Add the moto to the database """
        registration_result = db.Add_moto(moto)

        if registration_result:
            flash('Moto added successfully!')
            return redirect(url_for('add_moto'))
        else:
            flash('Failed to add the moto. Please try again.')
            return redirect(url_for('add_moto'))

    else:
        # Handle the GET request
        gps_records = db.get_all_gps_records()

        if gps_records is not None:
            return render_template('add_moto.html', available_gps_records=gps_records)
        else:
            flash('Failed to retrieve GPS records. Please try again later.')
            return redirect(url_for('add_moto'))

@app.route('/moto_information', methods=['GET'])
def moto_information():
    db = Database(db_config)
    moto_data = db.get_moto_data(db.db_connection)  # Call it on the db instance
    db.close_connection()
    return render_template('moto_information_template.html', moto_data=moto_data)

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
