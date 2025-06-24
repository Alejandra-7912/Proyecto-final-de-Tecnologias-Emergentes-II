from flask import Blueprint, session, flash, redirect, url_for, request
from views import personal_view, solicitud_licencia_view
from views import licencia_aprobada_view, comunicado_view, historial_view
from controllers.auth_controller import login_required
from models.usuario_model import Usuario
from models.empleado_model import Empleado
from models.solicitud_licencia_model import SolicitudLicencia
from models.licencia_aprobada_model import LicenciaAprobada
from models.historial_model import Historial
from models.comunicado_model import Comunicado
from models.tipo_licencia_model import TipoLicencia

from datetime import datetime, date

personal_bp = Blueprint("personal", __name__, url_prefix="/personal")


# acceso solo para el rol "personal"
@personal_bp.before_request
@login_required
def verificar_acceso():
    if session.get("user_role") != 3:  # 3: Personal
        flash("Acceso denegado. Solo personal autorizado.", "danger")
        return redirect(url_for("auth.login"))


# Dashboard principal
@personal_bp.route("/")
def dashboard():
    usuario_id = session.get("user_id")
    usuario = Usuario.get_by_id(usuario_id)
    
    if not usuario or not usuario.empleado_id:
        flash("Empleado no vinculado al usuario.", "danger")
        return redirect(url_for("auth.login"))

    empleado = Empleado.get_by_id(usuario.empleado_id)

    licencias_pendientes = LicenciaAprobada.query.filter_by(
        empleado_id=empleado.id, estado='Pendiente'
    ).count()

    return personal_view.dashboard(
        licencias_pendientes=licencias_pendientes,
    )

@personal_bp.route("/mi_perfil/")
def mi_perfil():
    usuario_id = session.get("user_id")
    usuario = Usuario.get_by_id(usuario_id)
    if not usuario:
        flash("Sesión inválida.", "danger")
        return redirect(url_for("auth.login"))

    empleado = Empleado.get_by_id(usuario.empleado_id)
    if not empleado:
        flash("Empleado no encontrado.", "warning")
        return redirect(url_for("personal.dashboard"))

    return personal_view.mi_perfil(empleado)

@personal_bp.route("/asistencia/marcar", methods=["GET", "POST"])
def marcar_asistencia():
    return personal_view.marcar_asistencia()

@personal_bp.route("/asistencia/historial")
def asistencia():
    return personal_view.ver_historial_asistencia()

@personal_bp.route("/solicitud_licencias/")
def permisos():
    return redirect(url_for("solicitud_licencia_personal.index_personal"))

@personal_bp.route("/licencias_aprobadas/")
def licencias_aprobadas():
    return redirect(url_for("licencia_aprobada_personal.index_por_estado", estado="Aprobada"))

@personal_bp.route("/comunicados/", methods=["GET"])
def comunicados():
    comunicados = Comunicado.get_all()
    return comunicado_view.personal_list(comunicados)

@personal_bp.route("/historial", methods=["GET"])
def historial():
    usuario_id = session.get("user_id")
    usuario = Usuario.get_by_id(usuario_id)

    if not usuario:
        flash("Sesión inválida.", "danger")
        return redirect(url_for("auth.login"))

    empleado_id = usuario.empleado_id
    historiales = Historial.get_by_empleado_id(empleado_id)

    return historial_view.personal_list(historiales)
