from flask import render_template

# ADMIN

def list(licencias):
    return render_template('admin/licencias_aprobadas/index.html', licencias=licencias)

def create(solicitud_licencias):
    return render_template(
        'admin/licencias_aprobadas/create.html',
        solicitud_licencias=solicitud_licencias
    )

def edit(licencia):
    return render_template(
        'admin/licencias_aprobadas/edit.html',
        licencia=licencia
    )

# DIRECTOR

def director_list(licencias):
    return render_template(
        "director/licencia_aprobada/index.html",
        licencias=licencias
    )

def director_edit(licencia_aprobada):
    return render_template(
        "director/licencias_aprobadas/edit.html",
        licencia_aprobada=licencia_aprobada
    )

# PERSONAL (solo listado)

def personal_list(licencias):
    return render_template(
        "personal/licencia_aprobada/index.html",
        licencias=licencias
    )
