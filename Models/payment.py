"""
Module: payment

This module defines the payment class, which represents a gps recovery&e-payment management system.
"""

class Payment():
    """
    Represents a payment done  in the recovery management system.

    Attributes:
         payment_id (int):payment's Id   
         customer_id:customer's id
         amount_paid: amount paid
         over_credit:over_credit
         balance: balance_credit
         payment_date:payment_date
         last_update:last_update
    """

    def __init__(self, customer_id, amount_paid, over_credit=0, balance=0):
        """
        Initialize a gps object.
        """
        self.customer_id = customer_id
        self.amount_paid = amount_paid
        self.over_credit = over_credit
        self.balance = balance
