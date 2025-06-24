from database import db
from sqlalchemy.orm import joinedload
from datetime import datetime

class Empleado(db.Model):
    __tablename__ = "empleados"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    apellido = db.Column(db.String(255), nullable=False)
    ci = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    telefono = db.Column(db.String(20), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    cargo_id = db.Column(db.Integer, db.ForeignKey('cargos.id'), nullable=False)

    cargo = db.relationship('Cargo', back_populates='empleados')
    usuarios = db.relationship('Usuario', back_populates='empleado', uselist=False) 
    asistencias = db.relationship('Asistencia', back_populates='empleado', cascade='all, delete-orphan')
    historial_laboral = db.relationship('Historial', back_populates='empleado', cascade='all, delete-orphan')
    licencias_aprobadas = db.relationship('LicenciaAprobada', back_populates='empleado', cascade='all, delete-orphan')
    solicitudes_licencia = db.relationship('SolicitudLicencia', back_populates='empleado', cascade='all, delete-orphan')

    def __init__(self, nombre, apellido, ci, email, telefono, fecha=None, cargo_id=None):
        self.nombre = nombre
        self.apellido = apellido
        self.ci = ci
        self.email = email
        self.telefono = telefono
        self.fecha = fecha if fecha else datetime.utcnow()
        self.cargo_id = cargo_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Empleado.query.all()

    @staticmethod
    def get_by_id(id):
        return Empleado.query.get(id)

    @staticmethod
    def get_full_by_id(id):
        return Empleado.query.options(
            joinedload(Empleado.cargo),
            joinedload(Empleado.usuarios),
            joinedload(Empleado.solicitudes_licencia),
            joinedload(Empleado.asistencias),
            joinedload(Empleado.licencias_aprobadas),
            joinedload(Empleado.historial_laboral)
        ).filter_by(id=id).first()

    @classmethod
    def get_by_usuario_id(cls, usuario_id):
        from models.usuario_model import Usuario
        usuario = Usuario.query.get(usuario_id)
        return usuario.empleado if usuario else None

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
