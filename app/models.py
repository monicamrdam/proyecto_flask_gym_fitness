from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModelMixin:
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)

    @classmethod
    def simple_filter(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()


class User(db.Model, BaseModelMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100))
    usuario = db.Column(db.String(100), nullable=False)
    hash_password = db.Column(db.String(10), nullable=False)
    mail = db.Column(db.String(100), nullable=False)
    datos_biometricos = db.relationship('DatosBiometricos', backref='user_associated_bio', lazy=True)
    datos_nutricionales = db.relationship('DatosNutricionales', backref='user_associated_nutri', lazy=True)
    rutinas = db.relationship('Rutina', backref='user_associated_rutina', lazy=True)

    def __repr__(self):
        return 'User id: {}, nombre: {}, mail: {}'.format(self.user_id, self.nombre, self.mail)


class DatosBiometricos(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    peso = db.Column(db.Float(10, 2), nullable=False)
    altura = db.Column(db.Float(10, 2), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    user = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)


class DatosNutricionales(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, nullable=False)
    dieta = db.Column(db.Text, nullable=False)
    user = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)

# febrero 2021,  maquina biceps
# febrero 2021, maquina triceps
# febrero 2021,  maquina biceps


class Rutina(db.Model, BaseModelMixin):
    rutina_id = db.Column(db.Integer, primary_key=True)
    rutina_nombre = db.Column(db.String(100))
    fecha_inicial = db.Column(db.DateTime, nullable=False)
    fecha_final = db.Column(db.DateTime, nullable=False)
    user = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    maquinas = db.relationship('RutinaMaquinaAssociation', back_populates='rutina')


class Maquina(db.Model, BaseModelMixin):
    maquina_id = db.Column(db.Integer, primary_key=True)
    maquina_nombre = db.Column(db.String(100), nullable=False)
    maquina_localizacion = db.Column(db.String(30), nullable=False)
    fecha_instalacion = db.Column(db.DateTime, nullable=False)
    rutinas = db.relationship('RutinaMaquinaAssociation', back_populates='maquina')


class RutinaMaquinaAssociation(db.Model, BaseModelMixin):
    rutina_id = db.Column(db.Integer, db.ForeignKey('Rutina.rutina_id'), primary_key=True)
    maquina_id = db.Column(db.Integer, db.ForeignKey('Maquina.maquina_id'), primary_key=True)
    rutina = db.relationship('Rutina', back_populates='maquinas')
    maquina = db.relationship('Maquina', back_populates='rutinas')
    num_ciclo = db.Column(db.Integer)
    num_repeticiones = db.Column(db.Integer)
