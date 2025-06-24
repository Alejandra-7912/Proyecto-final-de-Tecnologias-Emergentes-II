from flask import request, redirect, url_for, Blueprint, jsonify
from models.historial_model import Historial
from models.empleado_model import Empleado
from models.usuario_model import Usuario
from views import historial_view
from datetime import datetime

historial_bp = Blueprint('historial', __name__, url_prefix='/historiales')
historial_director_bp = Blueprint('historial_director', __name__, url_prefix='/director/historiales')

@historial_bp.route('/')
def index():
    historiales = Historial.get_all()
    return historial_view.list(historiales)


@historial_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        empleado_id = int(request.form['empleado_id'])
        empleado = Empleado.get_by_id(empleado_id)
        if not empleado:
            return "Empleado no encontrado", 404

        cargo = empleado.cargo.cargo if empleado.cargo else "Sin cargo"
        fecha_inicio = datetime.strptime(request.form['fecha_inicio'], '%Y-%m-%d').date()
        fecha_fin_str = request.form.get('fecha_fin')
        fecha_fin = datetime.strptime(fecha_fin_str, '%Y-%m-%d').date() if fecha_fin_str else None
        usuario_id = 1 

        historial = Historial(empleado_id, cargo, fecha_inicio, fecha_fin)
        historial.usuario_id = usuario_id
        historial.save()
        return redirect(url_for('historial.index'))

    empleados = Empleado.query.all()
    usuarios = Usuario.query.all()
    return historial_view.create(empleados=empleados, usuarios=usuarios)


@historial_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    historial = Historial.get_by_id(id)
    if not historial:
        return "Historial no encontrado", 404

    if request.method == 'POST':
        empleado_id = int(request.form['empleado_id'])
        empleado = Empleado.get_by_id(empleado_id)
        if not empleado:
            return "Empleado no encontrado", 404

        cargo = empleado.cargo.cargo if empleado.cargo else "Sin cargo"
        fecha_inicio = datetime.strptime(request.form['fecha_inicio'], '%Y-%m-%d').date()
        fecha_fin_str = request.form.get('fecha_fin')
        fecha_fin = datetime.strptime(fecha_fin_str, '%Y-%m-%d').date() if fecha_fin_str else None

        historial.update(
            empleado_id=empleado_id,
            cargo=cargo,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            usuario_id=historial.usuario_id
        )
        return redirect(url_for('historial.index'))

    empleados = Empleado.query.all()
    usuarios = Usuario.query.all()
    return historial_view.edit(historial=historial, empleados=empleados, usuarios=usuarios)


@historial_bp.route('/delete/<int:id>')
def delete(id):
    historial = Historial.get_by_id(id)
    if historial:
        historial.delete()
    return redirect(url_for('historial.index'))

# --------------------- Empleado ---------------------

@historial_bp.route('/imprimir/<int:empleado_id>')
def imprimir_historial(empleado_id):
    empleado = Empleado.get_by_id(empleado_id)
    if not empleado:
        return "Empleado no encontrado", 404

    return historial_view.imprimir(
    empleado=empleado,
    historial_laboral=empleado.historial_laboral,
    usuarios=[empleado.usuarios] if empleado.usuarios else [],
    asistencias=empleado.asistencias,
    licencias_aprobadas=empleado.licencias_aprobadas,
    solicitudes_licencia=empleado.solicitudes_licencia
)

@historial_bp.route('/empleado/<int:empleado_id>')
def get_empleado_json(empleado_id):
    empleado = Empleado.get_full_by_id(empleado_id)
    if not empleado:
        return jsonify({'error': 'Empleado no encontrado'}), 404

    data = {
        'nombre': empleado.nombre,
        'apellido': empleado.apellido,
        'ci': empleado.ci,
        'email': empleado.email,
        'telefono': empleado.telefono,
        'fecha': empleado.fecha.strftime('%Y-%m-%d'),
        'cargo': empleado.cargo.cargo if empleado.cargo else 'Sin cargo',
        'usuarios': [empleado.usuarios.username] if empleado.usuarios else []
    }
    return jsonify(data)

# --------------------- DIRECTOR ---------------------
@historial_director_bp.route('/')
def index_director():
    historiales = Historial.get_all()
    return historial_view.director_list(historiales)


@historial_director_bp.route('/imprimir/<int:empleado_id>')
def imprimir_director(empleado_id):
    empleado = Empleado.get_by_id(empleado_id)
    if not empleado:
        return "Empleado no encontrado", 404

    return historial_view.imprimir_director(
    empleado=empleado,
    historial_laboral=empleado.historial_laboral,
    usuarios=[empleado.usuarios] if empleado.usuarios else [],  
    asistencias=empleado.asistencias,
    licencias_aprobadas=empleado.licencias_aprobadas,
    solicitudes_licencia=empleado.solicitudes_licencia
)

