from flask import render_template, session, request, redirect, url_for, flash
from models.usuario_model import Usuario
from models.empleado_model import Empleado
from models.solicitud_licencia_model import SolicitudLicencia
from models.asistencia_model import Asistencia
from datetime import datetime, date
from sqlalchemy import and_

# 👉 Dashboard principal
def dashboard(licencias_pendientes=0):
    usuario_id = session.get("user_id")
    usuario = Usuario.get_by_id(usuario_id)

    if not usuario:
        flash("Sesión inválida.", "danger")
        return redirect(url_for("auth.login"))

    empleado = Empleado.get_by_id(usuario.empleado_id)
    if not empleado:
        flash("Empleado no encontrado.", "danger")
        return redirect(url_for("auth.login"))

    rol_usuario = usuario.rol.rol.strip().lower() 

    return render_template("personal/dashboard.html",
                           licencias_pendientes=licencias_pendientes,
                           empleado=empleado,
                           rol_usuario=rol_usuario,
                           fecha_actual=datetime.now().strftime('%d/%m/%Y'))

# 👉 Mostrar perfil
def mi_perfil(empleado):
    if not empleado:
        return "Empleado no encontrado", 404
    return render_template("personal/mi_perfil.html", empleado=empleado)

# 👉 Marcar asistencia (entrada/salida)
def marcar_asistencia():
    usuario_id = session.get("user_id")
    usuario = Usuario.get_by_id(usuario_id)

    if not usuario:
        flash("Sesión inválida.", "danger")
        return redirect(url_for("auth.login"))

    empleado_id = usuario.empleado_id
    hoy = date.today()

    asistencia = Asistencia.query.filter(
        and_(Asistencia.fecha == hoy, Asistencia.empleado_id == empleado_id)
    ).first()

    if request.method == "POST":
        ahora = datetime.now().time()

        if not asistencia:
            nueva = Asistencia(
                fecha=hoy,
                hora_entrada=ahora,
                empleado_id=empleado_id
            )
            nueva.save()
            flash("Entrada registrada exitosamente.", "success")
        elif not asistencia.hora_salida:
            asistencia.hora_salida = ahora
            asistencia.save()
            flash("Salida registrada exitosamente.", "success")
        else:
            flash("Ya marcaste entrada y salida hoy.", "warning")

        return redirect(url_for("personal.marcar_asistencia"))

    return render_template("personal/asistencia/marcar.html", asistencia=asistencia)

# 👉 Historial de asistencias
def ver_historial_asistencia():
    usuario_id = session.get("user_id")
    usuario = Usuario.get_by_id(usuario_id)

    if not usuario:
        flash("Sesión inválida.", "danger")
        return redirect(url_for("auth.login"))

    empleado_id = usuario.empleado_id
    historial = Asistencia.query.filter_by(
        empleado_id=empleado_id
    ).order_by(Asistencia.fecha.desc()).all()

    return render_template("personal/asistencia/historial.html", historial=historial)

