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
    def Add_customer(self, customer):
        """
        Insert a new customer into the database.

        Args:
            customer (Customer): The Customer object to be inserted into the database.
        """
        cursor = self.db_connection.cursor()
        insert_query = """
            INSERT INTO customer(first_name, last_name, email, active)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(insert_query, (customer.first_name, customer.last_name, customer.email, customer.active))
        self.db_connection.commit()
        cursor.close()
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
