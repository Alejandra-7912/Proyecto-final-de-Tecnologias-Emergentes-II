from flask import Flask,request
import os
#----------------admin-------------------------------
from controllers import cargo_controller
from controllers import empleado_controller
from controllers import asistencia_controller
from controllers import comunicado_controller
from controllers import tipo_licencia_controller
from controllers import licencia_aprobada_controller
from controllers import solicitud_licencia_controller
from controllers import rol_controller
from controllers import usuario_controller
from controllers import historial_controller

#----------------principal----------------------------
from controllers import home_controller
from controllers import admin_controller
from controllers import director_controller
from controllers import personal_controller
from controllers import auth_controller
#-----------------------------------------------------

from database import db

app = Flask(__name__)
app.config["SECRET_KEY"] = "miclavesecreta"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///control_personalv1.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


#------------------------------------------------------
db.init_app(app)
#------------------------------------------------------


#-------------------------admin----------------------------
app.register_blueprint(usuario_controller.usuario_bp)
app.register_blueprint(rol_controller.rol_bp)
app.register_blueprint(cargo_controller.cargo_bp)
app.register_blueprint(empleado_controller.empleado_bp)
app.register_blueprint(asistencia_controller.asistencia_bp)
app.register_blueprint(comunicado_controller.comunicado_bp)
app.register_blueprint(tipo_licencia_controller.tipo_licencia_bp)
app.register_blueprint(licencia_aprobada_controller.licencia_aprobada_bp)
app.register_blueprint(solicitud_licencia_controller.solicitud_licencia_bp)
app.register_blueprint(historial_controller.historial_bp)

#-------------------------Direc----------------------------
app.register_blueprint(empleado_controller.empleado_director_bp)
app.register_blueprint(tipo_licencia_controller.tipo_licencia_director_bp)
app.register_blueprint(licencia_aprobada_controller.licencia_aprobada_director_bp)
app.register_blueprint(solicitud_licencia_controller.solicitud_licencia_director_bp)
app.register_blueprint(comunicado_controller.comunicado_director_bp)
app.register_blueprint(historial_controller.historial_director_bp)

#-------------------------Pers----------------------------
app.register_blueprint(personal_controller.personal_bp)
app.register_blueprint(solicitud_licencia_controller.solicitud_licencia_personal_bp)
app.register_blueprint(licencia_aprobada_controller.licencia_aprobada_personal_bp)

#-----------------------------------------------------
app.register_blueprint(home_controller.home_bp)
app.register_blueprint(admin_controller.admin_bp)
app.register_blueprint(director_controller.director_bp)
app.register_blueprint(auth_controller.auth_bp)

#-----------------------------------------------------


@app.context_processor
def inject_active_path():
    def is_active(path):
        return 'active' if request.path == path else ''
    return(dict(is_active = is_active))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)