from flask import Blueprint, request, render_template

user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/register', methods=['GET','POST'])
def register_user():

    if request.methods == 'POST':
        pass

    return render_template('users/register.html')