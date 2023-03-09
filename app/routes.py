from flask import render_template, redirect, url_for
from flask_login import current_user
from app import app
from app.forms import LoginForm
from app.models import User


@app.route('/')
@app.route('/index')
def index():
    u = User.get_all()
    print(u)
    return render_template('index.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()

    # True si el usuario ha hecho submit del formulario
    if form.validate_on_submit():
        pass

    return render_template('login.html', form=form)
