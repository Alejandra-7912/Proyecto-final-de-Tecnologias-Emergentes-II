from database import db

class TipoLicencia(db.Model):
    __tablename__ = 'tipos_licencia'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(200))

    solicitudes = db.relationship('SolicitudLicencia', back_populates='tipo_licencia', cascade='all, delete-orphan')

    def __init__(self, nombre, descripcion=None):
        self.nombre = nombre
        self.descripcion = descripcion

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return TipoLicencia.query.all()

    @staticmethod
    def get_by_id(id):
        return TipoLicencia.query.get(id)

    def update(self, nombre=None, descripcion=None):
        if nombre:
            self.nombre = nombre
        if descripcion is not None:
            self.descripcion = descripcion
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
