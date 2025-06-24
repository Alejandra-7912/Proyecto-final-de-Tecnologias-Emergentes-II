from database import db

class Historial(db.Model):
    __tablename__ = "historial_laboral"

    id = db.Column(db.Integer, primary_key=True)
    empleado_id = db.Column(db.Integer, db.ForeignKey('empleados.id'), nullable=False)
    cargo = db.Column(db.String(100), nullable=False)
    fecha_inicio = db.Column(db.Date, nullable=False)
    fecha_fin = db.Column(db.Date)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)


    empleado = db.relationship('Empleado', back_populates='historial_laboral')
    usuario = db.relationship('Usuario', back_populates='historiales')

    def __init__(self, empleado_id, cargo, fecha_inicio, fecha_fin=None):
        self.empleado_id = empleado_id
        self.cargo = cargo
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Historial.query.all()

    @staticmethod
    def get_by_id(id):
        return Historial.query.get(id)
    
    @staticmethod
    def get_by_empleado_id(empleado_id):
        return Historial.query.filter_by(empleado_id=empleado_id).order_by(Historial.fecha_inicio.desc()).all()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
