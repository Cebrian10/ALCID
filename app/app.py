from flask import Flask, render_template, request, redirect, url_for, flash
from config import config

from flask_login import LoginManager, login_user, logout_user, login_required

import pyodbc

from Models.ModelUser import ModelUser
from Models.entities.User import User

app = Flask(__name__)

server = 'ALDAIR'
database = 'proy_flask'
username = 'Cebrian10'
password = 'lizmariham507'

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                        f'SERVER={server};'
                        f'DATABASE={database};'
                        f'UID={username};'
                        f'PWD={password}')

login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(conn, id)

@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(conn, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                #print(user.username)
                return redirect(url_for('home'))
            else:
                flash("Constraseña invalida...")
                return render_template('auth/login.html')
        else:
            flash("Usuario no encontrado...")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run(debug=True, port=5000)