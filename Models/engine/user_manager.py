from Models.engine.db_manager import Database
from Models.user import User

class UserManager:
    """
    A class for managing user registration and login.

    Attributes:
        db (Database): An instance of the Database class for database interactions.
    """

    def __init__(self, db_config):
        """
        Initialize the UserManager with a database connection.
        """
        self.db = Database(db_config)
    def register_user(self, user):
        """
        Register a new user with the provided User object and store their information in the database.

        Args:
            user (User): User object with attributes like email and password.

        Returns:
            str: A registration success message or an error message.
        """
        # Check if the user already exists
        existing_user = self.db.fetch_one("SELECT * FROM users WHERE username = %s", (user.username,))
        if existing_user:
            return "username already in use."

        # Use the insert_user method to insert the new user into the database
        try:
            self.db.insert_user(user)
            return "Registration successful!"
        except Exception as e:
            print(f"Error registering user: {str(e)}")
            return "Registration failed. Please try again later."
    def login_user(self, username, password):
        """
        Authenticate a user's login and return a success message or an error message.

        Args:
            username (str): User's username.
            password (str): User's password (plaintext).

        Returns:
            tuple: A tuple containing a login success message (or an error message) and user data.
        """
        # Retrieve the user's information from the database
        user_data = self.db.fetch_one("SELECT * FROM users WHERE username = %s", (username,))
        print("User data:", user_data)
        if user_data is not None:
            # The 'fetch_one' method likely returns a tuple, so you should access elements by index
            db_password = user_data[7]  # Assuming that the password is at the 7th position (0-based index) in the tuple
            role = user_data[4]
            if db_password == password:
                return "Login successful!", user_data  # Return both the success message and user data
            else:
                return "Incorrect password.", None  # Return an error message and None for user data
        else:
            return "Username not found.", None  # Return an error message and None for user data

    def close_database_connection(self):
        """
        Close the database connection when it's no longer needed.
        """
        self.db.close()
