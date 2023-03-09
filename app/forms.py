from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, PasswordField, BooleanField, SubmitField


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={"placeholder": "username"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "password"})
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Submit')