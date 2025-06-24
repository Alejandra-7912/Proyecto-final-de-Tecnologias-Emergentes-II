from flask import request, redirect, url_for, Blueprint, flash,session
from models.licencia_aprobada_model import LicenciaAprobada
from models.empleado_model import Empleado
from models.solicitud_licencia_model import SolicitudLicencia
from models.tipo_licencia_model import TipoLicencia
from views import licencia_aprobada_view

licencia_aprobada_bp = Blueprint('licencia_aprobada', __name__, url_prefix='/licencias_aprobadas')
licencia_aprobada_director_bp = Blueprint('licencia_aprobada_director', __name__, url_prefix='/director/licencias_aprobadas')
licencia_aprobada_personal_bp = Blueprint('licencia_aprobada_personal', __name__, url_prefix='/personal/licencias_aprobadas')


# ---------- ADMIN ---------- #
@licencia_aprobada_bp.route('/')
def index():
    licencias = LicenciaAprobada.get_all()
    return licencia_aprobada_view.list(licencias)

@licencia_aprobada_bp.route('/estado/<string:estado>')
def index_por_estado(estado):
    licencias = LicenciaAprobada.get_by_estado(estado)
    return licencia_aprobada_view.list(licencias)

@licencia_aprobada_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        try:
            solicitud_licencia_id = int(request.form['solicitud_licencia_id'])
            estado = request.form.get('estado', 'Pendiente')

            solicitud = SolicitudLicencia.get_by_id(solicitud_licencia_id)
            if not solicitud:
                flash("Solicitud no encontrada", "danger")
                return redirect(url_for('licencia_aprobada.create'))

            licencia = LicenciaAprobada(
                empleado_id=solicitud.empleado_id,
                solicitud_licencia_id=solicitud.id,
                estado=estado
            )
            licencia.save()
            flash("Licencia aprobada creada correctamente.", "success")
            return redirect(url_for('licencia_aprobada.index'))
        except Exception as e:
            flash(f"Error al crear licencia aprobada: {str(e)}", "danger")

    solicitudes = SolicitudLicencia.get_all()
    return licencia_aprobada_view.create(solicitudes)

@licencia_aprobada_bp.route('/cambiar_estado/<int:id>/<string:nuevo_estado>')
def cambiar_estado(id, nuevo_estado):
    licencia = LicenciaAprobada.get_by_id(id)
    if not licencia:
        flash("Licencia no encontrada", "danger")
    else:
        try:
            licencia.update(estado=nuevo_estado)
            flash(f"Estado de la licencia actualizado a {nuevo_estado}.", "success")
        except Exception as e:
            flash(f"Error al actualizar estado: {str(e)}", "danger")

    return redirect(url_for('licencia_aprobada.index'))


@licencia_aprobada_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    licencia = LicenciaAprobada.get_by_id(id)
    if not licencia:
        return "Licencia aprobada no encontrada", 404

    if request.method == 'POST':
        try:
            estado = request.form.get('estado')

            licencia.update(estado=estado)
            flash("Licencia aprobada actualizada correctamente.", "success")
            return redirect(url_for('licencia_aprobada.index'))
        except Exception as e:
            flash(f"Error al actualizar licencia: {str(e)}", "danger")

    return licencia_aprobada_view.edit(licencia)

@licencia_aprobada_bp.route('/delete/<int:id>')
def delete(id):
    licencia = LicenciaAprobada.get_by_id(id)
    if licencia:
        try:
            licencia.delete()
            flash("Licencia eliminada correctamente.", "success")
        except Exception as e:
            flash(f"Error al eliminar licencia: {str(e)}", "danger")
    else:
        flash("Licencia no encontrada.", "warning")
    return redirect(url_for('licencia_aprobada.index'))

# ---------- DIRECTOR ---------- #
@licencia_aprobada_director_bp.route('/')
def index_director():
    licencias = LicenciaAprobada.get_all()
    return licencia_aprobada_view.director_list(licencias)

@licencia_aprobada_director_bp.route('/estado/<string:estado>')
def index_por_estado(estado):
    licencias = LicenciaAprobada.get_by_estado(estado)
    return licencia_aprobada_view.director_list(licencias)

#------------- personal---------
@licencia_aprobada_personal_bp.route('/')
def index_personal():
    usuario_id = session.get("user_id")
    empleado = Empleado.get_by_usuario_id(usuario_id)
    
    if not empleado:
        flash("Empleado no encontrado.", "danger")
        return redirect(url_for("personal.dashboard"))
    
    licencias = LicenciaAprobada.get_by_empleado_id(empleado.id)
    return licencia_aprobada_view.personal_list(licencias)

@licencia_aprobada_personal_bp.route('/estado/<string:estado>')
def index_por_estado_personal(estado):
    usuario_id = session.get("user_id")
    empleado = Empleado.get_by_usuario_id(usuario_id)

    if not empleado:
        flash("Empleado no encontrado.", "danger")
        return redirect(url_for("personal.dashboard"))

    licencias = LicenciaAprobada.query.filter_by(
        empleado_id=empleado.id,
        estado=estado
    ).all()

    return licencia_aprobada_view.personal_list(licencias)
