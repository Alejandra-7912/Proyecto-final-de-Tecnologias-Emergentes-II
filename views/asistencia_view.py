from flask import render_template

def list(asistencias):
    return render_template('admin/asistencias/index.html', asistencias=asistencias)

def create():
    from models.empleado_model import Empleado
    empleados = Empleado.get_all()
    return render_template('admin/asistencias/create.html', empleados=empleados)

def edit(asistencia):
    from models.empleado_model import Empleado
    empleados = Empleado.get_all()
    return render_template('admin/asistencias/edit.html', asistencia=asistencia, empleados=empleados)
