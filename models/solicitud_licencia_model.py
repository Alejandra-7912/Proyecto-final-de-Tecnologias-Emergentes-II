from database import db
from datetime import date

class SolicitudLicencia(db.Model):
    __tablename__ = "solicitudes_licencia"

    id = db.Column(db.Integer, primary_key=True)
    fecha_solicitud = db.Column(db.Date, default=date.today, nullable=False)
    fecha_inicio = db.Column(db.Date, nullable=False)
    fecha_fin = db.Column(db.Date, nullable=False)
    motivo = db.Column(db.Text, nullable=False)
    empleado_id = db.Column(db.Integer, db.ForeignKey('empleados.id'), nullable=False)
    tipo_licencia_id = db.Column(db.Integer, db.ForeignKey('tipos_licencia.id'), nullable=False)

    empleado = db.relationship('Empleado', back_populates='solicitudes_licencia')
    tipo_licencia = db.relationship('TipoLicencia', back_populates='solicitudes')
    licencia_aprobada = db.relationship('LicenciaAprobada', back_populates='solicitud_licencia', uselist=False)

    def __init__(self, fecha_solicitud, fecha_inicio, fecha_fin, motivo, empleado_id, tipo_licencia_id):
        self.fecha_solicitud = fecha_solicitud
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.motivo = motivo
        self.empleado_id = empleado_id
        self.tipo_licencia_id = tipo_licencia_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return SolicitudLicencia.query.all()

    @staticmethod
    def get_by_id(id):
        return SolicitudLicencia.query.get(id)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
