from flask import render_template

def render_dashboard(total_empleados=0, licencias_pendientes=0, total_comunicados=0):
    return render_template(
        "director/dashboard.html",
        total_empleados=total_empleados,
        licencias_pendientes=licencias_pendientes,
        total_comunicados=total_comunicados
    )
