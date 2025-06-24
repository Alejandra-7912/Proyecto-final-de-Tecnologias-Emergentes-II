from flask import request, redirect, url_for, Blueprint, flash
from models.empleado_model import Empleado
from models.cargo_model import Cargo
from views import empleado_view
from datetime import datetime

empleado_bp = Blueprint('empleado', __name__, url_prefix="/empleados")
empleado_director_bp = Blueprint('empleado_director', __name__, url_prefix="/director/empleados")

@empleado_bp.route("/")
def index():
    empleados = Empleado.get_all()
    return empleado_view.list(empleados)

@empleado_bp.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            apellido = request.form['apellido']
            ci = request.form['ci']
            email = request.form['email']
            telefono = request.form['telefono']
            fecha = datetime.strptime(request.form['fecha'], "%Y-%m-%d")
            cargo_id = int(request.form['cargo_id'])

            empleado = Empleado(
                nombre=nombre,
                apellido=apellido,
                ci=ci,
                email=email,
                telefono=telefono,
                fecha=fecha,
                cargo_id=cargo_id
            )

            empleado.save()
            flash('Empleado creado correctamente.', 'success')

            return redirect(url_for('empleado.index'))

        except Exception as e:
            flash(f'Error al crear empleado: {str(e)}', 'danger')

    cargos = Cargo.get_all()
    return empleado_view.create(cargos)

@empleado_bp.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    empleado = Empleado.get_by_id(id)
    if not empleado:
        return "Empleado no encontrado", 404

    if request.method == 'POST':
        try:
            empleado.update(
                nombre=request.form['nombre'],
                apellido=request.form['apellido'],
                ci=request.form['ci'],
                email=request.form['email'],
                telefono=request.form['telefono'],
                fecha=datetime.strptime(request.form['fecha'], "%Y-%m-%d"),
                cargo_id=int(request.form['cargo_id'])
            )
            flash('Empleado actualizado correctamente.', 'success')
            return redirect(url_for('empleado.index'))
        except Exception as e:
            flash(f'Error al actualizar empleado: {str(e)}', 'danger')

    cargos = Cargo.get_all()
    return empleado_view.edit(empleado, cargos)

@empleado_bp.route("/delete/<int:id>")
def delete(id):
    empleado = Empleado.get_by_id(id)
    if empleado:
        try:
            empleado.delete()
            flash('Empleado eliminado correctamente.', 'success')
        except Exception as e:
            flash(f'Error al eliminar empleado: {str(e)}', 'danger')
    else:
        flash('Empleado no encontrado.', 'warning')
    return redirect(url_for('empleado.index'))

#-------------Director---------------
@empleado_director_bp.route("/")
def index_director():
    empleados = Empleado.get_all()
    return empleado_view.director_list(empleados)

@empleado_director_bp.route("/create", methods=['GET', 'POST'])
def create_director():
    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            apellido = request.form['apellido']
            ci = request.form['ci']
            email = request.form['email']
            telefono = request.form['telefono']
            fecha = datetime.strptime(request.form['fecha'], "%Y-%m-%d")
            cargo_id = int(request.form['cargo_id'])

            empleado = Empleado(
                nombre=nombre,
                apellido=apellido,
                ci=ci,
                email=email,
                telefono=telefono,
                fecha=fecha,
                cargo_id=cargo_id
            )

            empleado.save()
            flash('Empleado creado correctamente.', 'success')
            return redirect(url_for('empleado_director.index_director'))

        except Exception as e:
            flash(f'Error al crear empleado: {str(e)}', 'danger')

    cargos = Cargo.get_all()
    return empleado_view.director_create(cargos)

@empleado_director_bp.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit_director(id):
    empleado = Empleado.get_by_id(id)
    if not empleado:
        return "Empleado no encontrado", 404

    if request.method == 'POST':
        try:
            empleado.update(
                nombre=request.form['nombre'],
                apellido=request.form['apellido'],
                ci=request.form['ci'],
                email=request.form['email'],
                telefono=request.form['telefono'],
                fecha=datetime.strptime(request.form['fecha'], "%Y-%m-%d"),
                cargo_id=int(request.form['cargo_id'])
            )
            flash('Empleado actualizado correctamente.', 'success')
            return redirect(url_for('empleado_director.index_director'))
        except Exception as e:
            flash(f'Error al actualizar empleado: {str(e)}', 'danger')

    cargos = Cargo.get_all()
    return empleado_view.director_edit(empleado, cargos)

@empleado_director_bp.route("/delete/<int:id>")
def delete_director(id):
    empleado = Empleado.get_by_id(id)
    if empleado:
        try:
            empleado.delete()
            flash('Empleado eliminado correctamente.', 'success')
        except Exception as e:
            flash(f'Error al eliminar empleado: {str(e)}', 'danger')
    else:
        flash('Empleado no encontrado.', 'warning')
    return redirect(url_for('empleado_director.index_director'))
