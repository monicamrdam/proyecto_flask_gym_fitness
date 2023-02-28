from app.models import User#, Rutina, Maquina, RutinaMaquinaAssociation


def fill_users():
    u = User(user_id=1, nombre='Monica', apellido='', usuario='monica_23', hash_password='wefbuib12333',
             mail='example@mail.com')
    print(u)
    User.insert(u)

'''
def fill_rutinas_maquinas():
    aso_obj = RutinaMaquinaAssociation(rutina_id=1, maquina_id=1, num_ciclo=4, num_repeticiones=20)
    rutina = Rutina(rutina_id=1, rutina_nombre='marzo 2023', fecha_inicial='2023-03-01', fecha_final='2023-04-01')
    maquina = Maquina(maquina_id=1, maquina_nombre='Biceps')

    aso_obj.rutina = rutina
    aso_obj.maquina = maquina

    rutina.maquinas.append(aso_obj)
    maquina.rutinas.append(aso_obj)

    print(rutina)
    Rutina.insert(rutina)

    print(maquina)
    Maquina.insert(maquina)

    print(aso_obj)
    RutinaMaquinaAssociation.insert(aso_obj)
'''


