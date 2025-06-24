from flask import render_template

def list(comunicados):
    return render_template('admin/comunicado/index.html', comunicados=comunicados)

def create():
    return render_template('admin/comunicado/create.html')


def edit(comunicado ):
    return render_template('admin/comunicado/edit.html', comunicado=comunicado)


#----------director--------

def director_list(comunicados):
    return render_template("director/comunicado/index.html", comunicados=comunicados)

def director_create():
    return render_template("director/comunicado/create.html")

def director_edit(comunicado):
    return render_template("director/comunicado/edit.html", comunicado=comunicado)

#-----------personal-------


def personal_list(comunicados):
    return render_template("personal/comunicado/index.html", comunicados=comunicados)
