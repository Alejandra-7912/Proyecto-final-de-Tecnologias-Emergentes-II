from database import db

class Rol(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    rol = db.Column(db.String(80), nullable=False)
    usuarios = db.relationship('Usuario', back_populates='rol', cascade='all, delete-orphan')

    def __init__(self, rol):
        self.rol = rol

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Rol.query.all()

    @staticmethod
    def get_by_id(id):
        return Rol.query.get(id)

    def update(self, rol=None):
        if rol:
            self.rol = rol
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
