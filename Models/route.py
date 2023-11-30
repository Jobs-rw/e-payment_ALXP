from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {
    'user1': 'password1',
    'user2': 'password2'
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in users and users[username] == password:
        # Authentication successful, redirect to a new page or perform further actions
        return f"Welcome, {username}!"
    else:
        # Authentication failed, redirect back to the login page with a message
        return render_template('login.html', message='Invalid credentials. Please try again.')

if __name__ == '__main__':
    app.run(debug=True)
