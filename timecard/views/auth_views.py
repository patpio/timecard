from flask import Blueprint, render_template, url_for, flash, request
from flask_login import login_user, logout_user
from werkzeug.utils import redirect

from timecard import db
from ..models import User
from ..forms import SignUpForm, LoginForm

bp_auth = Blueprint('auth', __name__, url_prefix='/auth')


@bp_auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))

    return render_template('signup.html', form=form)


@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_by_username(form.username.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, form.remember_me.data)
            flash(f'Logged in successfully as {user.username}')
            return redirect(request.args.get('next') or url_for('main.home', username=user.username))

    return render_template('login.html', form=form)


@bp_auth.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('main.home'))
