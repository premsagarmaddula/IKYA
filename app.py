from flask import Flask, request, render_template, redirect, url_for # type: ignore

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Retrieve form data
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Example logic: Check credentials (replace with your logic)
        if username == "admin" and password == "password":
            return "Login Successful"
        else:
            return "Invalid Credentials, please try again."
    
    # Render the login form for GET requests
    return render_template('login.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/teams')
def teams():
    return render_template('teams.html')

@app.route('/index')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
