"""
Module: database_manager

This module defines the Database class, which provides functionality for interacting
with a MySQL database for a stock management system.
"""
import mysql.connector

db_config = {
    'user': 'root',
    'password': 'jobs123',
    'host': 'localhost',
    'database': 'e_payment'
}

connection = mysql.connector.connect(**db_config)

class Database:
    """
    A class for interacting with a MySQL database.

    Attributes:
        db_connection: The MySQL database connection.
    """

    def __init__(self, db_config):
        """
        Initialize the Database class with the provided database configuration.

        Args:
            db_config (dict): A dictionary containing database connection parameters,
                such as 'user', 'password', 'host', and 'database'.
        """
        self.db_connection = mysql.connector.connect(**db_config)
        self.cursor = self.db_connection.cursor()


    def query(self, sql, values=None):
        self.cursor.execute(sql, values)
        result = self.cursor.fetchall()
        return result

    def execute(self, sql, values=None):
        self.cursor.execute(sql, values)
        self.db_connection.commit()

    def insert_user(self, user):
        """
        Insert a new user into the database.

        Args:
            user (User): The User object to be inserted into the database.
        """
        cursor = self.db_connection.cursor()
        insert_query = """
            INSERT INTO users(first_name, last_name, email, phone, role, username, password)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (user.first_name, user.last_name, user.email, user.phone, user.role, user.username, user.password))
        self.db_connection.commit()
        cursor.close()
        
    def get_user_by_id(self, user_id):
        """will help us to get user before üpdate users by User_id"""
        query = "SELECT * FROM users WHERE id = %s"
        user = self.fetch_one(query, (user_id,))

        if user:
            # Assuming you have a User class defined
            return User(
                id=user[0],
                email=user[1],
                username=user[2],
                password=user[3],
                role=user[4],
                first_name=user[5],
                last_name=user[6],
                phone=user[7]
            )
        else:
            return None

    def update_user(self, user_id, first_name, last_name, email, username, role, phone):
        """Update user information in the database."""
        query = """
            UPDATE users
            SET first_name = %s, last_name = %s, email = %s, username = %s, role = %s, phone = %s
            WHERE id = %s
        """
        values = (first_name, last_name, email, username, role, phone, user_id)
        try:
            self.execute(query, values)
            # Commit the changes
            self.commit()
            return True  # Update successful
        except Exception as e:
            print(f"Error updating user: {e}")
            # Handle the error or log it
            return False  # Update failed

    def get_user_data(self, connection):
        """this method will retrieve the customer from database and display the on the form"""
        query = "SELECT * FROM users"
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute(query)
            user_data = cursor.fetchall()
        return user_data


    def Add_customer(self, customer):
        """
        Insert a new customer into the database.

        Args:
            customer (Customer): The Customer object to be inserted into the database.
        """
        cursor = self.db_connection.cursor()
        gps_id = self.get_gps_id_by_EMEI(customer.gps_id)
        insert_query = """
            INSERT INTO customer(first_name, last_name, email, active, gps_id)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (customer.first_name, customer.last_name, customer.email, customer.active, customer.gps_id))
        self.db_connection.commit()
        cursor.close()

    def update_customer(self, customer_id, first_name, last_name, email, active):
        """Update customer information in the database."""
        query = """
            UPDATE customers
            SET first_name = %s, last_name = %s, email = %s, active = %s
            WHERE id = %s
        """
        values = (first_name, last_name, email, active, customer_id)
        try:
            self.execute(query, values)
            # Commit the changes
            self.commit()
            return True  # Update successful
        except Exception as e:
            print(f"Error updating customer: {e}")
            # Handle the error or log it
            return False  # Update failed

    def get_all_customers(self):
        """
        Retrieve all customer data from the database.

        Returns:
            list: A list containing dictionaries with customer information.
        """
        query = "SELECT * FROM customer"
        customers = self.fetch_all(query)
        return customers


    def get_customer_by_id(self, customer_id):
        """Fetch customer information by ID from the database."""
        query = "SELECT * FROM customers WHERE id = %s"
        values = (customer_id,)
        return self.fetch_one(query, values)

    def Add_GPS(self, GPS):
        """
        Insert a new gps into the database.

        Args:
            GPS (GPSTracker): The gps object to be inserted into the database.
        """
        cursor = self.db_connection.cursor()
        insert_query = """
            INSERT INTO gps(EMEI, Model_Name, Activated_date, GPS_Experied_date)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(insert_query, (GPS.EMEI, GPS.Model_Name, GPS.Activated_date, GPS.GPS_Experied_date))
        self.db_connection.commit()
        cursor.close()
        
    def fetch_all(self, query):
        """method handles executing the query and fetching all records from the database"""
        try:
            cursor = self.db_connection.cursor(dictionary=True)
            cursor.execute(query)
            records = cursor.fetchall()
            return records
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None  # Return None in case of an error
        finally:
            if 'cursor' in locals() and cursor is not None:
                cursor.close()

    def get_all_gps_records(self):
        query = 'SELECT gps_id, EMEI, Model_Name, Activated_date, GPS_Experied_date FROM gps'
        gps_records = self.fetch_all(query)
        print(gps_records)  # You can use this print statement for debugging
        return gps_records

    def get_gps_id_by_EMEI(self, EMEI):
        cursor = self.db_connection.cursor()
        select_query = "SELECT gps_id FROM gps WHERE EMEI = %s"
        cursor.execute(select_query, (EMEI,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return result[0]
        else:
            # Handle the case when EMEI is not found
            return None

    def get_gps_data(self, connection):
        try:
            with connection.cursor() as cursor:
                query = "SELECT * FROM gps"
                cursor.execute(query)
                gps_data = cursor.fetchall()
                print("GPS Data:", gps_data)
                return gps_data
        except Exception as e:
            print(f"Error retrieving GPS data: {e}")
            return None
        
    def Add_moto(self, moto):
        """
        Insert a new moto into the database.

        Args:
            moto (Moto): The Moto object to be inserted into the database.
        """
        cursor = self.db_connection.cursor()
        gps_id = self.get_gps_id_by_EMEI(moto.gps_id)
        insert_query = """
            INSERT INTO moto(plate, chassis_Number, Engine_Number, Model, gps_id)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (moto.plate, moto.Chassis_Number, moto.Engine_Number, moto.Model, moto.gps_id))
        self.db_connection.commit()
        cursor.close()

    def get_moto_data(self, connection):
        cursor = None
        try:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM moto"  # Update this query to match your schema
            cursor.execute(query)
            moto_data = cursor.fetchall()
            return moto_data
        except Exception as e:
            print(f"Error executing query: {e}")
            print(f"SQL Query: {query}")
            # Print the traceback
            import traceback
            traceback.print_exc()
            return None
        finally:
            if cursor is not None:
                cursor.close()

    def close_connection(self):
        """
        Close the database connection.
        """
        self.db_connection.close()

    def fetch_one(self, query, params=None):
        """
        Execute a SQL query and fetch a single row.

        Args:
            query (str): The SQL query to execute.
            params (tuple): A tuple of parameters to be used with the query.

        Returns:
            dict: A dictionary representing a single row from the result.
        """
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            result = self.cursor.fetchone()
            self.db_connection.commit()  # Update this line
            return result
        except Exception as e:
            print(f"Error: {str(e)}")
            self.db_connection.rollback()  # Update this line
            return None
