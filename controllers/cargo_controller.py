from flask import request, redirect, url_for, Blueprint
from models.cargo_model import Cargo
from views import cargo_view

cargo_bp = Blueprint('cargo', __name__, url_prefix='/cargos')

@cargo_bp.route('/')
def index():
    cargos = Cargo.get_all()
    return cargo_view.list(cargos)

@cargo_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        cargo = request.form['cargo']
        descripcion = request.form.get('descripcion')

        nuevo_cargo = Cargo(cargo, descripcion)
        nuevo_cargo.save()
        return redirect(url_for('cargo.index'))
    
    return cargo_view.create()

@cargo_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    cargo = Cargo.get_by_id(id)
    if not cargo:
        return "Cargo no encontrado", 404

    if request.method == 'POST':
        nuevo_cargo = request.form['cargo']
        nueva_descripcion = request.form.get('descripcion')

        cargo.update(cargo=nuevo_cargo, descripcion=nueva_descripcion)
        return redirect(url_for('cargo.index'))

    return cargo_view.edit(cargo)

@cargo_bp.route('/delete/<int:id>')
def delete(id):
    cargo = Cargo.get_by_id(id)
    if cargo:
        cargo.delete()
    return redirect(url_for('cargo.index'))
