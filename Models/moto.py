#from base_model import BaseModel

"""
Module: customers

This module defines the User class, which represents a user in the stock management system.
"""

class Moto():
    """
    Represents a moto in recovery  management system.

    Attributes:
        moto_id (int): The moto's id.
        chassis_Number (varchar): The moto's chassis_Number.
        engine_Number (varchar): moto's engine_Number.
        Model (varchar): The moto's Model.
    """

    def __init__(self, plate, Model, Chassis_Number,Engine_Number, gps_id):
        """
        Initialize a User object.

        Args:
        moto_id (int): The moto's id.
        chassis_Number (varchar): The moto's chassis_Number.
        engine_Number (varchar): moto's engine_Number.
        Model (varchar): The moto's Model.
        gps_id (foreign key) from gps table

        """
        self.plate = plate
        self.Model = Model
        self.Chassis_Number = Chassis_Number
        self.Engine_Number = Engine_Number
        self.gps_id = gps_id

