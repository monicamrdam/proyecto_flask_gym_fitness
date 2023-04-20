from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={"placeholder": "username"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "password"})
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Submit')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={"placeholder": "username"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "email"})

    nombre = StringField('Nombre', validators=[DataRequired()], render_kw={"placeholder": "name"})
    apellido = StringField('Primer apellido', render_kw={"placeholder": "surname"})

    password = PasswordField('password', validators=[DataRequired(), EqualTo('password2')],
                             render_kw={"placeholder": "password"})
    password2 = PasswordField('confirm password', validators=[DataRequired()],
                              render_kw={"placeholder": "confirm password"})
    submit = SubmitField('Register')

    def validate_username(self, username):
        # Comprobar que no existe ningun usuario con ese usename
        user = User.query.filter_by(usuario=username.data).first()
        print(user)
        if user is not None:
            raise ValidationError('Error, ese username ya existe, usa uno diferente.')

    def validate_email(self, email):
        #  Comprobar que no existe ningun usuario con ese email
        user = User.query.filter_by(mail=email.data).first()
        print(user)
        if user is not None:
            raise ValidationError('Error, este mail ya se encuentra en uso.')
