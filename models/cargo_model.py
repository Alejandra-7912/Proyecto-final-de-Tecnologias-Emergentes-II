from database import db

class Cargo(db.Model):
    __tablename__ = "cargos"

    id = db.Column(db.Integer, primary_key=True)
    cargo = db.Column(db.String(80), nullable=False)
    descripcion = db.Column(db.Text)
    
    empleados = db.relationship('Empleado', back_populates='cargo')

    def __init__(self, cargo, descripcion=None):
        self.cargo = cargo
        self.descripcion = descripcion

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Cargo.query.all()

    @staticmethod
    def get_by_id(id):
        return Cargo.query.get(id)

    def update(self, cargo=None, descripcion=None):
        if cargo:
            self.cargo = cargo
        if descripcion:
            self.descripcion = descripcion
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
