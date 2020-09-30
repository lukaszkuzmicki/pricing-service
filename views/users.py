from flask import Blueprint, request, render_template, session

from models.user.user import User, UserErrors

user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        try:
            User.register_user(email, password)
            # how to send some data to broweser? like user hash --> we are sending cookies  we flasku uzywamy 'session'
            session['email'] = email  # zapisujemy do sesji emaila
            return email
        except UserErrors.UserError as e:
            return e.message

    return render_template('users/register.html')

@user_blueprint.route('/login', methods=['GET','POST'])
def login_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            if User.is_login_valid(email, password):
                session['email'] = email
                return email
        except UserErrors.UserError as e:
            return e.message



    return render_template('users/login.html')

@user_blueprint.route('logout')
def logout():
    session['email'] = None
    return render_template('users/login.html')






