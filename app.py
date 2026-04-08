from flask import Flask, render_template, request, redirect, url_for
import os
import datetime

app = Flask(__name__)

# Ensure logs directory exists
LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lab", "captured_clicks.log")

def log_interaction(username):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        # Logging that a user submitted data (we don't log the password for ethical reasons)
        f.write(f"[{timestamp}] ALERT: Phishing link clicked and submitted by: {username}\n")

@app.route('/')
def index():
    # Serve the bait page
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    # password = request.form.get('password') # We don't store passwords in simulations
    
    log_interaction(username)
    print(f"[!] PHISHING ALERT: User {username} submitted credentials.")
    
    # Redirect to the educational warning page
    return redirect('/warning')

@app.route('/warning')
def warning():
    # Serve the educational "Gotcha" page
    return render_template('warning.html')

if __name__ == '__main__':
    # Crucial: Ensure the templates are found correctly
    print("[*] Starting Phishing Awareness Simulation at http://127.0.0.1:5000")
    app.run(port=5000)
