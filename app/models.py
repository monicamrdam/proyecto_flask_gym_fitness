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
    datos_biometricos = db.relationship('DatosBiometricos', backref='user_associated', lazy=True)

    def __repr__(self):
        return 'User id: {}, nombre: {}, mail: {}'.format(self.user_id, self.nombre, self.mail)


class DatosBiometricos(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    peso = db.Column(db.Float(10, 2))
    altura = db.Column(db.Float(10, 2))
    fecha = db.Column(db.DateTime, nullable=False)
    user = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)

