from flask import Blueprint, render_template
from flask_login import login_required

bp_user = Blueprint('user', __name__, url_prefix='/users')


@bp_user.route('/user')
@login_required
def user():
    return render_template('user.html')
