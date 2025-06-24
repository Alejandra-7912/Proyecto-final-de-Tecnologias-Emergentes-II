from flask import render_template

# ---------------------- ADMIN ----------------------

def list(solicitudes):
    return render_template('admin/solicitud_licencias/index.html', solicitudes=solicitudes)

def create(empleados, tipos, fecha_actual):
    return render_template('admin/solicitud_licencias/create.html', empleados=empleados, tipos=tipos, fecha_actual=fecha_actual)

def edit(solicitud, empleados, tipos):
    return render_template('admin/solicitud_licencias/edit.html', solicitud=solicitud, empleados=empleados, tipos=tipos)

# ---------------------- DIRECTOR ----------------------

def director_list(solicitudes):
    return render_template('director/solicitud_licencias/index.html', solicitudes=solicitudes)

def director_create(empleados, tipos, fecha_actual):
    return render_template('director/solicitud_licencias/create.html', empleados=empleados, tipos=tipos, fecha_actual=fecha_actual)

def director_edit(solicitud, empleados, tipos):
    return render_template('director/solicitud_licencias/edit.html', solicitud=solicitud, empleados=empleados, tipos=tipos)

# ---------------------- PERSONAL ----------------------
def personal_list(solicitudes):
    return render_template('personal/solicitud_licencias/index.html', solicitudes=solicitudes)

def personal_create( tipos, fecha_actual):
    return render_template('personal/solicitud_licencias/create.html', tipos=tipos, fecha_actual=fecha_actual)

def personal_edit(solicitud, tipos):
    return render_template('personal/solicitud_licencias/edit.html', solicitud=solicitud, tipos=tipos)
