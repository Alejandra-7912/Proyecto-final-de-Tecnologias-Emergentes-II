from flask import render_template

def list(usuarios):
    return render_template('admin/usuarios/index.html', usuarios=usuarios)

def create(empleados, roles):
    return render_template('admin/usuarios/create.html', empleados=empleados, roles=roles)

def edit(usuario, empleados, roles):
    return render_template('admin/usuarios/edit.html', usuario=usuario, empleados=empleados, roles=roles)
