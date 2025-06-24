from database import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    empleado_id = db.Column(db.Integer, db.ForeignKey('empleados.id'), nullable=False)
    rol_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)

    rol = db.relationship('Rol', back_populates='usuarios')
    empleado = db.relationship('Empleado', back_populates='usuarios')
    comunicados = db.relationship('Comunicado', back_populates='usuario', cascade='all, delete-orphan')
    historiales = db.relationship('Historial', back_populates='usuario', cascade='all, delete-orphan')

    def __init__(self, username, password, empleado_id, rol_id):
        self.username = username
        self.password = self.hash_password(password)
        self.empleado_id = empleado_id
        self.rol_id = rol_id

    @staticmethod
    def hash_password(password):
        return generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Usuario.query.all()

    @staticmethod
    def get_by_id(id):
        return Usuario.query.get(id)

    def update(self, username=None, password=None, empleado_id=None, rol_id=None):
        if username:
            self.username = username
        if password:
            self.password = self.hash_password(password)
        if empleado_id:
            self.empleado_id = empleado_id
        if rol_id:
            self.rol_id = rol_id
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
