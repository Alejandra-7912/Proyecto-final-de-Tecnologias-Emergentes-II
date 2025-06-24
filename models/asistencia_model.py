from database import db
from datetime import date

class Asistencia(db.Model):
    __tablename__ = "asistencias"

    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False, default=date.today)
    hora_entrada = db.Column(db.Time)
    hora_salida = db.Column(db.Time)
    justificacion = db.Column(db.Text)

    empleado_id = db.Column(db.Integer, db.ForeignKey('empleados.id'), nullable=False)
    empleado = db.relationship('Empleado', back_populates='asistencias')

    def __init__(self, fecha=None, hora_entrada=None, hora_salida=None, justificacion=None, empleado_id=None):
        self.fecha = fecha or date.today()
        self.hora_entrada = hora_entrada
        self.hora_salida = hora_salida
        self.justificacion = justificacion
        self.empleado_id = empleado_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Asistencia.query.all()

    @staticmethod
    def get_by_id(id):
        return Asistencia.query.get(id)

    def update(self, fecha=None, hora_entrada=None, hora_salida=None, justificacion=None, empleado_id=None):
        if fecha:
            self.fecha = fecha
        if hora_entrada:
            self.hora_entrada = hora_entrada
        if hora_salida:
            self.hora_salida = hora_salida
        if justificacion:
            self.justificacion = justificacion
        if empleado_id:
            self.empleado_id = empleado_id
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
