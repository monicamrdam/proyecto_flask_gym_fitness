from flask import render_template

from app import app
from app.models import User


@app.route('/')
@app.route('/index')
def index():
    u = User.get_all()
    print(u)
    return render_template('index.html', title='Home')
