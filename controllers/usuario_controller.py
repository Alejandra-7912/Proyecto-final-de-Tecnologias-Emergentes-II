from flask import request, redirect, url_for, Blueprint
from models.usuario_model import Usuario
from models.empleado_model import Empleado
from models.rol_model import Rol
from views import usuario_view

usuario_bp = Blueprint('usuario', __name__, url_prefix="/usuarios")

@usuario_bp.route("/")
def index():
    usuarios = Usuario.get_all()
    return usuario_view.list(usuarios)

@usuario_bp.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        empleado_id = request.form['empleado_id']
        rol_id = request.form['rol_id']
        usuario = Usuario(username, password, empleado_id, rol_id)
        usuario.save()
        return redirect(url_for('usuario.index'))

    empleados = Empleado.get_all()
    roles = Rol.get_all()
    return usuario_view.create(empleados, roles)

@usuario_bp.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    usuario = Usuario.get_by_id(id)
    if not usuario:
        return "Usuario no encontrado", 404

    if request.method == 'POST':
        username = request.form['username']
        password = request.form.get('password') 
        rol_id = request.form['rol_id']
        empleado_id = request.form['empleado_id']

        usuario.update(
            username=username,
            password=password if password else None, 
            rol_id=rol_id,
            empleado_id=empleado_id
        )
        return redirect(url_for('usuario.index'))
    
    empleados = Empleado.get_all()
    roles = Rol.get_all()
    return usuario_view.edit(usuario, empleados, roles)


@usuario_bp.route("/delete/<int:id>")
def delete(id):
    usuario = Usuario.get_by_id(id)
    if usuario:
        usuario.delete()
    return redirect(url_for('usuario.index'))