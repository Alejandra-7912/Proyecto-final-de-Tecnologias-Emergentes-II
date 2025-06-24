from flask import Blueprint, redirect, url_for, session, flash
from views.director_view import render_dashboard
from .auth_controller import login_required
from models.empleado_model import Empleado
from models.solicitud_licencia_model import SolicitudLicencia
from models.licencia_aprobada_model import LicenciaAprobada
from models.comunicado_model import Comunicado

director_bp = Blueprint("director", __name__, url_prefix="/director")

@director_bp.before_request
@login_required
def verificar_acceso():
    # Verificar si el usuario es director (rol_id == 2)
    if session.get("user_role") != 2:
        flash("Acceso denegado. Debes ser directoristrador para acceder.", "danger")
        return redirect(url_for("auth.login"))

@director_bp.route("/")
def dashboard():
    total_empleados = Empleado.query.count()
    licencias_pendientes = LicenciaAprobada.query.filter_by(estado='Pendiente').count()
    total_comunicados = Comunicado.query.count()

    return render_dashboard(
        total_empleados=total_empleados,
        licencias_pendientes=licencias_pendientes,
        total_comunicados=total_comunicados
    )

@director_bp.route("/comunicados/")
def comunicados():
    return redirect(url_for("comunicado.index"))

@director_bp.route("/licencias_aprobadas/")
def licencias_aprobadas():
    return redirect(url_for("licencia_aprobada.index"))

@director_bp.route("/historiales/")
def historiales():
    return redirect(url_for("historial.index"))

@director_bp.route("/empleados/")
def empleados():
    return redirect(url_for("empleado.index"))

@director_bp.route("/solicitud_licencias/")
def permisos():
    return redirect(url_for("solicitud_licencia_director.index_director"))
