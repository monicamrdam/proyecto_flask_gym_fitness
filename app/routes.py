from flask import render_template, redirect, url_for
from flask_login import current_user, login_user
from app import app, login
from app.forms import LoginForm
from app.models import User


@login.user_loader
def load_user(id):
    return User.get_by_id(int(id))


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
        # el usuario con ese username existe
        # la contraseña es correcta
        user = User.filter_by(usuario=form.username.data).first()

        # el usuario existe
        if user is not None:
            # comprobar que la contraseña es correcta
            if user.check_password(form.password.data):
                login_user(user, remember=form.remember_me.data)
                return redirect(url_for('index'))
            else:
                print('Mensaje de error')
        else:
            print('Mensaje de error ')
    return render_template('login.html', form=form)
