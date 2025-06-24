from flask import render_template
from models.empleado_model import Empleado
from models.asistencia_model import Asistencia
from models.solicitud_licencia_model import SolicitudLicencia
from models.comunicado_model import Comunicado
from sqlalchemy import func
from datetime import date

def render_dashboard(total_empleados=0, asistencias_hoy=0, licencias_pendientes=0, total_comunicados=0,
                     ultimas_asistencias=None, licencias_recientes=None):
    return render_template(
        "admin/dashboard.html",
        total_empleados=total_empleados,
        asistencias_hoy=asistencias_hoy,
        licencias_pendientes=licencias_pendientes,
        total_comunicados=total_comunicados,
        ultimas_asistencias=ultimas_asistencias,
        licencias_recientes=licencias_recientes
    )
