from flask import render_template

#------ ADMIN
def list(tipos):
    return render_template("admin/tipo_licencia/index.html", tipos=tipos)

def create():
    return render_template("admin/tipo_licencia/create.html")

def edit(tipo):
    return render_template("admin/tipo_licencia/edit.html", tipo=tipo)

#------ DIRECTOR
def director_list(tipos):
    return render_template("director/tipo_licencia/index.html", tipos=tipos)

def director_create():
    return render_template("director/tipo_licencia/create.html")

def director_edit(tipo):
    return render_template("director/tipo_licencia/edit.html", tipo=tipo)
