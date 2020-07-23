# First we import Flask

from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps
# Create the application object

app = Flask(__name__)
app.secret_key = "master password"

# Use decorators to link function to a page


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/welcome')
def welcome():
    return render_template('login.html')


# Creating login page


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again.'
        else:
            session['logged_in'] = True
            flash("You were logged in!")
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged in', None)
    flash("You were logged out!")
    return redirect(url_for('welcome'))



# Start the server with the run method

                                                            
if __name__ == '__main__':
    app.run(debug=True)