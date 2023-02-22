from app.models import User


def fill_users():
    u = User(user_id=1, nombre='Monica', apellido='', usuario='monica_23', hash_password='wefbuib12333',
             mail='example@mail.com')
    print(u)
    User.insert(u)