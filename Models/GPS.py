"""
Module: GPS

This module defines the GPS class, which represents a gps recovery&e-payment management system.
"""

class GPSTracker():
    """
    Represents a gps in the recovery management system.

    Attributes:
        EMEI (int): The gps's EMEI.
        GPS Model (str): The gps's Model.
        activated_date (date): The gps 's activated_date.
         gps_expired_date(date): gps_expired_date
    """

    def __init__(self, EMEI, Model_Name, Activated_date, GPS_Experied_date):
        """
        Initialize a gps object.
        """
        self.EMEI = EMEI
        self.Model_Name = Model_Name
        self.Activated_date = Activated_date
        self.GPS_Experied_date = GPS_Experied_date
        self.id = id
    def extend_expiration(self, years=0, months=0, days=0):
        # Extend the expiration date by the specified duration
        new_expired_date = self.GPS_experied_date + timedelta(days=days, months=months, years=years)
        self.GPS_experied_date = new_expired_date
