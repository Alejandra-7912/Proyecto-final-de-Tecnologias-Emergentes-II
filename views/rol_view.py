from flask import render_template

def list(roles):
    return render_template("admin/roles/index.html", roles=roles)

def create():
    return render_template("admin/roles/create.html")

def edit(rol):
    return render_template("admin/roles/edit.html", rol=rol)
