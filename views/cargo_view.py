from flask import render_template

def list(cargos):
    return render_template("admin/cargos/index.html", cargos=cargos)

def create():
    return render_template("admin/cargos/create.html")

def edit(cargo):
    return render_template("admin/cargos/edit.html", cargo=cargo)
