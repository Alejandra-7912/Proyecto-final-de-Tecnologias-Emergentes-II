from flask import render_template

def list(empleados):
    return render_template("admin/empleados/index.html", empleados=empleados)

def create(cargos):
    return render_template("admin/empleados/create.html", cargos=cargos)

def edit(empleado, cargos):
    return render_template("admin/empleados/edit.html", empleado=empleado, cargos=cargos)

#-------------------director----------------------

def director_list(empleados):
    return render_template("director/empleados/index.html", empleados=empleados)

def director_create(cargos):
    return render_template("director/empleados/create.html", cargos=cargos)

def director_edit(empleado, cargos):
    return render_template("director/empleados/edit.html", empleado=empleado, cargos=cargos)

