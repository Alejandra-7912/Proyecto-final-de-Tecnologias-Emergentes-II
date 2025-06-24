from database import db
from sqlalchemy.orm import joinedload 

class LicenciaAprobada(db.Model):
    __tablename__ = "licencias_aprobadas"

    id = db.Column(db.Integer, primary_key=True)
    empleado_id = db.Column(db.Integer, db.ForeignKey('empleados.id'), nullable=False)
    solicitud_licencia_id = db.Column(db.Integer, db.ForeignKey('solicitudes_licencia.id'))
    estado = db.Column(db.String(20), nullable=True)

    empleado = db.relationship('Empleado', back_populates='licencias_aprobadas')
    solicitud_licencia = db.relationship('SolicitudLicencia', back_populates='licencia_aprobada')

    def __init__(self, empleado_id, solicitud_licencia_id, estado='Pendiente'):
        self.empleado_id = empleado_id
        self.solicitud_licencia_id = solicitud_licencia_id
        self.estado = estado

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return LicenciaAprobada.query.options(
            joinedload(LicenciaAprobada.empleado),
            joinedload(LicenciaAprobada.solicitud_licencia)
        ).all()

    @staticmethod
    def get_by_id(id):
        return LicenciaAprobada.query.get(id)

    @staticmethod
    def get_by_estado(estado):
        from models.empleado_model import Empleado
        from models.solicitud_licencia_model import SolicitudLicencia

        return LicenciaAprobada.query \
            .filter_by(estado=estado) \
            .join(Empleado).join(SolicitudLicencia) \
            .options(
                joinedload(LicenciaAprobada.empleado),
                joinedload(LicenciaAprobada.solicitud_licencia)
            ).all()

    def update(self, empleado_id=None, solicitud_licencia_id=None, estado=None):
        if empleado_id:
            self.empleado_id = empleado_id
        if solicitud_licencia_id:
            self.solicitud_licencia_id = solicitud_licencia_id
        if estado:
            self.estado = estado
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
