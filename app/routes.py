from flask import render_template, redirect, url_for
from flask_login import current_user, login_user
from app import app, login
from app.forms import LoginForm, RegisterForm
from app.models import User
from flask_login import login_required, logout_user

'''
Vistas

- Vista insertar datos biometricos (formulario)
- Vista historico datos biometricos
- Vista insertar dieta (formulario)
- Vista lista de dietas
- Vista seleccion rutinas disponibles
'''

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
        print(form.username.data)
        user = User.query.filter_by(usuario=form.username.data).first()
        print(user)

        # el usuario existe
        if user is not None:
            # comprobar que la contraseña es correcta
            if user.check_password(form.password.data):
                login_user(user, remember=form.remember_me.data)
                return redirect(url_for('index'))
            else:
                print('contraseña incorrecta')
        else:
            print('usuario no existe')
    else:
        print('error validacion')
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    # Crearemos el formulario
    form = RegisterForm()

    # Validar el formulario
    if form.validate_on_submit():
        # Crear un nuevo usuario
        user = User(usuario=form.username.data, mail=form.email.data, nombre=form.nombre.data,
                    apellido=form.apellido.data)
        print(user)
        user.set_password(form.password.data)
        User.insert(user)
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))