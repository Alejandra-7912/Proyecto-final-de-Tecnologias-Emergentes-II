from flask import request, redirect, url_for, Blueprint
from models.asistencia_model import Asistencia
from views import asistencia_view
from datetime import datetime

asistencia_bp = Blueprint('asistencia', __name__, url_prefix='/asistencias')

@asistencia_bp.route('/')
def index():
    asistencias = Asistencia.get_all()
    return asistencia_view.list(asistencias)

@asistencia_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        fecha_str = request.form['fecha']
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()

        hora_entrada_str = request.form['hora_entrada']
        hora_entrada = datetime.strptime(hora_entrada_str, '%H:%M').time()

        hora_salida_str = request.form.get('hora_salida')
        hora_salida = None
        if hora_salida_str:
            hora_salida = datetime.strptime(hora_salida_str, '%H:%M').time()

        justificacion = request.form.get('justificacion')
        empleado_id = request.form['empleado_id']

        asistencia = Asistencia(fecha, hora_entrada, hora_salida, justificacion, empleado_id)
        asistencia.save()
        return redirect(url_for('asistencia.index'))

    return asistencia_view.create()


from datetime import datetime

@asistencia_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    asistencia = Asistencia.get_by_id(id)
    if not asistencia:
        return "Asistencia no encontrada", 404

    if request.method == 'POST':
        fecha_str = request.form['fecha']
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()

        hora_entrada_str = request.form['hora_entrada']
        hora_entrada = datetime.strptime(hora_entrada_str, '%H:%M').time()

        hora_salida_str = request.form.get('hora_salida')
        hora_salida = None
        if hora_salida_str:
            hora_salida = datetime.strptime(hora_salida_str, '%H:%M').time()

        justificacion = request.form.get('justificacion')
        empleado_id = request.form['empleado_id']

        asistencia.update(
            fecha=fecha,
            hora_entrada=hora_entrada,
            hora_salida=hora_salida,
            justificacion=justificacion,
            empleado_id=empleado_id
        )
        return redirect(url_for('asistencia.index'))

    return asistencia_view.edit(asistencia)

@asistencia_bp.route('/delete/<int:id>')
def delete(id):
    asistencia = Asistencia.get_by_id(id)
    if asistencia:
        asistencia.delete()
    return redirect(url_for('asistencia.index'))
