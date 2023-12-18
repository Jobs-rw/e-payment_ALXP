#from base_model import BaseModel

"""
Module: customers

This module defines the User class, which represents a user in the stock management system.
"""

class Customer():
    """
    Represents a customer in recovery  management system.

    Attributes:
        first_name (str): The customer's first name.
        last_name (str): The customer's last name.
        email (str): The customer's email address.
        phone (str): The customer's phone number.
        active(tinyint(1)) customer's status.
        create_date (datetime) customer's date created.
        last_update(datetime) customer's  date updated.
    """

    def __init__(self, first_name,last_name, email, active):
        """
        Initialize a User object.

        Args:
        first_name (str): The customer's first name.
        last_name (str): The customer's last name.
        email (str): The customer's email address.
        phone (str): The customer's phone number.
        active(tinyint(1)) customer's status.
        create_date (datetime) customer's date created.
        last_update(datetime) customer's  date updated.

        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.active = active
