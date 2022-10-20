from flask import Flask, render_template, url_for, redirect
import ibm_db
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt

# database details
# cant create a db because it is not free :(

hostname = "myhostname"
uid="username"
password ="password"
driver="driver name"
dbname = "db2"
port="5000"
protocol = "TCPIP"

dsn=("DRIVER={0};""DATABASE={1};""HOSTNAME={2};""PORT={3};""PROTOCOL={4};""UID={5};""PWD={6};").format(driver,dbname,hostname,port,protocol,uid,password)
try:
    db = DB2.connect(dsn,"","")
    print("Connected to database")
except:
    print("Unable to connect")
app = Flask(__name__)

bcrypt = Bcrypt(app)
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/logout')
@login_required
def logout():
 
    return redirect(url_for('login'))


@ app.route('/register')
def register():

    return render_template('register.html')

if __name__ == "__main__":
    app.run(debug=True)
