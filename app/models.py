from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
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


class User(UserMixin, db.Model, BaseModelMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100))
    usuario = db.Column(db.String(100), nullable=False)
    hash_password = db.Column(db.String(128), nullable=False)
    mail = db.Column(db.String(120), nullable=False)
    datos_biometricos = db.relationship('DatosBiometricos', backref='user_associated_bio', lazy=True)
    datos_nutricionales = db.relationship('DatosNutricionales', backref='user_associated_nutri', lazy=True)
    rutinas = db.relationship('Rutina', backref='user_associated_rutina', lazy=True)

    def __repr__(self):
        return 'User id: {}, nombre: {}, mail: {}'.format(self.user_id, self.nombre, self.mail)

    def set_password(self, password):
        self.hash_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hash_password, password)


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


class RutinaMaquinaAssociation(db.Model, BaseModelMixin):
    rutina_id = db.Column(db.Integer, db.ForeignKey('rutina.rutina_id'), primary_key=True)
    maquina_id = db.Column(db.Integer, db.ForeignKey('maquina.maquina_id'), primary_key=True)
    num_ciclo = db.Column(db.Integer)
    num_repeticiones = db.Column(db.Integer)
    rutina = db.relationship('Rutina', back_populates='maquinas')
    maquina = db.relationship('Maquina', back_populates='rutinas')


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



