from flask import Blueprint, render_template

bp_user = Blueprint('users', __name__, url_prefix='/users')


@bp_user.route('/user')
def user():
    return render_template('user.html')
