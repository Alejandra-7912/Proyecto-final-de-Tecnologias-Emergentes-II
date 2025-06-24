from database import db
from datetime import date, datetime

class Comunicado(db.Model):
    __tablename__ = "comunicados"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    contenido = db.Column(db.Text, nullable=False)
    fecha_publicacion = db.Column(db.Date, nullable=False, default=date.today)
    
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    usuario = db.relationship('Usuario', back_populates='comunicados')

    def __init__(self, titulo, contenido, fecha_publicacion=None, usuario_id=None):
        self.titulo = titulo
        self.contenido = contenido
        self.fecha_publicacion = fecha_publicacion or date.today()
        self.usuario_id = usuario_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Comunicado.query.all()

    @staticmethod
    def get_by_id(id):
        return Comunicado.query.get(id)

    def update(self, titulo=None, contenido=None, fecha_publicacion=None, usuario_id=None):
        if titulo:
            self.titulo = titulo
        if contenido:
            self.contenido = contenido
        if fecha_publicacion:
            self.fecha_publicacion = fecha_publicacion
        if usuario_id:
            self.usuario_id = usuario_id
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def convert_to_date(date_str):
        """Convierte un string en formato 'YYYY-MM-DD' a un objeto date."""
        try:
            return datetime.strptime(date_str, '%Y-%m-%d').date()
        except (ValueError, TypeError):
            return None 
