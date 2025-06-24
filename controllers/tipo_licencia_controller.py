from flask import request, redirect, url_for, Blueprint, flash
from models.tipo_licencia_model import TipoLicencia
from views import tipo_licencia_view

tipo_licencia_bp = Blueprint('tipo_licencia', __name__, url_prefix='/tipos_licencia')
tipo_licencia_director_bp = Blueprint('tipo_licencia_director', __name__, url_prefix='/director/tipos_licencia')

#-------------------- ADMIN --------------------#
@tipo_licencia_bp.route('/')
def index():
    tipos = TipoLicencia.get_all()
    return tipo_licencia_view.list(tipos)

@tipo_licencia_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            descripcion = request.form.get('descripcion')

            tipo = TipoLicencia(nombre=nombre, descripcion=descripcion)
            tipo.save()
            flash("Tipo de licencia creado correctamente.", "success")
            return redirect(url_for('tipo_licencia.index'))

        except Exception as e:
            flash(f"Error al crear tipo de licencia: {str(e)}", "danger")

    return tipo_licencia_view.create()

@tipo_licencia_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    tipo = TipoLicencia.get_by_id(id)
    if not tipo:
        return "Tipo de licencia no encontrado", 404

    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            descripcion = request.form.get('descripcion')

            tipo.update(nombre=nombre, descripcion=descripcion)
            flash("Tipo de licencia actualizado correctamente.", "success")
            return redirect(url_for('tipo_licencia.index'))

        except Exception as e:
            flash(f"Error al actualizar tipo de licencia: {str(e)}", "danger")

    return tipo_licencia_view.edit(tipo)

@tipo_licencia_bp.route('/delete/<int:id>')
def delete(id):
    tipo = TipoLicencia.get_by_id(id)
    if tipo:
        try:
            tipo.delete()
            flash("Tipo de licencia eliminado correctamente.", "success")
        except Exception as e:
            flash(f"Error al eliminar tipo de licencia: {str(e)}", "danger")
    else:
        flash("Tipo de licencia no encontrado.", "warning")
    return redirect(url_for('tipo_licencia.index'))

#-------------------- DIRECTOR --------------------#
@tipo_licencia_director_bp.route('/')
def index_director():
    tipos = TipoLicencia.get_all()
    return tipo_licencia_view.director_list(tipos)

@tipo_licencia_director_bp.route('/create', methods=['GET', 'POST'])
def create_director():
    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            descripcion = request.form.get('descripcion')

            tipo = TipoLicencia(nombre=nombre, descripcion=descripcion)
            tipo.save()
            flash("Tipo de licencia creado correctamente.", "success")
            return redirect(url_for('tipo_licencia_director.index_director'))

        except Exception as e:
            flash(f"Error al crear tipo de licencia: {str(e)}", "danger")

    return tipo_licencia_view.director_create()

@tipo_licencia_director_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_director(id):
    tipo = TipoLicencia.get_by_id(id)
    if not tipo:
        return "Tipo de licencia no encontrado", 404

    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            descripcion = request.form.get('descripcion')

            tipo.update(nombre=nombre, descripcion=descripcion)
            flash("Tipo de licencia actualizado correctamente.", "success")
            return redirect(url_for('tipo_licencia_director.index_director'))

        except Exception as e:
            flash(f"Error al actualizar tipo de licencia: {str(e)}", "danger")

    return tipo_licencia_view.director_edit(tipo)

@tipo_licencia_director_bp.route('/delete/<int:id>')
def delete_director(id):
    tipo = TipoLicencia.get_by_id(id)
    if tipo:
        try:
            tipo.delete()
            flash("Tipo de licencia eliminado correctamente.", "success")
        except Exception as e:
            flash(f"Error al eliminar tipo de licencia: {str(e)}", "danger")
    else:
        flash("Tipo de licencia no encontrado.", "warning")
    return redirect(url_for('tipo_licencia_director.index_director'))
