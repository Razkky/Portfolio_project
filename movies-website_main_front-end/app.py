from flask import Flask, render_template
import json
from flask_cors import CORS

app = Flask(__name__)
core = CORS(app)

@app.route("/")
def home():
    """Home page"""
    return render_template("index1.html")

@app.route('/login', methods=["GET"], strict_slashes=False)
def login():
    """Login page"""
    print("login page")
    return render_template('login.html')

@app.route('/sign_up', methods=["GET"], strict_slashes=False)
def sign_up():
    """Sign up page"""
    return render_template('signUp.html')

@app.route('/dashboard', methods=["GET"], strict_slashes=False)
def dashboard():
    """Dashboard page"""
    return render_template('dashboard.html')

@app.route('/profile', methods=["GET"], strict_slashes=False)
def profile():
    """Set up profile page"""
    return render_template('profile.html')

@app.route('/forget_password', methods=['GET'], strict_slashes=False)
def forget():
    """Forget password page"""
    return render_template('forget_password.html')

@app.route('/reset_password/<token>', methods=['GET'], strict_slashes=False)
def reset(token):
    """Reset password page"""
    return render_template('reset_password.html', token=token)

if __name__=="__main__":
    """Starts up flask application"""
    app.run(debug=True)
