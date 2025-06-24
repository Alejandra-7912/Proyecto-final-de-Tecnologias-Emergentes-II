from flask import request, redirect, url_for, Blueprint
from models.rol_model import Rol
from views import rol_view

rol_bp = Blueprint('rol', __name__, url_prefix="/roles")

@rol_bp.route("/")
def index():
    roles = Rol.get_all()
    return rol_view.list(roles)

@rol_bp.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nombre = request.form['rol']
        rol = Rol(nombre)
        rol.save()
        return redirect(url_for('rol.index'))
    
    return rol_view.create()

@rol_bp.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    rol = Rol.get_by_id(id)
    if not rol:
        return "Rol no encontrado", 404

    if request.method == 'POST':
        nuevo_nombre = request.form['rol']
        rol.update(rol=nuevo_nombre)
        return redirect(url_for('rol.index'))
    
    return rol_view.edit(rol)

@rol_bp.route("/delete/<int:id>")
def delete(id):
    rol = Rol.get_by_id(id)
    if rol:
        rol.delete()
    return redirect(url_for('rol.index'))
