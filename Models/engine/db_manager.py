"""
Module: database_manager

This module defines the Database class, which provides functionality for interacting
with a MySQL database for a stock management system.
"""

import mysql.connector
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mjabush@!33',
    database='e-payment'
)

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

    def close_connection(self):
        """
        Close the database connection.
        """
        self.db_connection.close()
