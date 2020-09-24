from flask import Blueprint, request, render_template, session

user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/register', methods=['GET','POST'])
def register_user():

    if request.methods == 'POST':
        email= request.form['email']
        password= request.form['password']

        try:
            User.reqister_user(email,password)
            #how to send some data to broweser? like user hash --> we are sending cookies  we flasku uzywamy 'session'
            session.email = email # zapisujemy do sesji emaila
        except Exception as e:
            return e.message

    return render_template('users/register.html')