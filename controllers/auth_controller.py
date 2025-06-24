from flask import Blueprint, redirect, url_for, request, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from functools import wraps
from models.usuario_model import Usuario
from models.empleado_model import Empleado 
from views.auth_view import render_login_form, render_register_form

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("Por favor, inicia sesión.", "warning")
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    return decorated_function

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        ci = request.form["ci"]
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        email = request.form["email"]
        telefono = request.form["telefono"]
        fecha_str = request.form["fecha_nacimiento"]

        rol_id = 3 
        cargo_id = 1 

        # Validar campos obligatorios
        if not username or not password or not email or not ci:
            flash("Completa los campos obligatorios.", "danger")
            return redirect(url_for("auth.register"))

        try:
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        except ValueError:
            flash("Formato de fecha inválido.", "danger")
            return redirect(url_for("auth.register"))

        # Validar existencia previa
        if Usuario.query.filter_by(username=username).first():
            flash("El nombre de usuario ya existe.", "danger")
            return redirect(url_for("auth.register"))

        if Empleado.query.filter_by(ci=ci).first():
            flash("Este número de CI ya está registrado.", "danger")
            return redirect(url_for("auth.register"))

        if Empleado.query.filter_by(email=email).first():
            flash("Este correo ya está registrado.", "danger")
            return redirect(url_for("auth.register"))

        # Crear registros
        nuevo_empleado = Empleado(
            ci=ci,
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono,
            fecha=fecha,
            cargo_id=cargo_id
        )
        nuevo_empleado.save()

        nuevo_usuario = Usuario(
            username=username,
            password=generate_password_hash(password),
            rol_id=rol_id,
            empleado_id=nuevo_empleado.id
        )
        nuevo_usuario.save()

        flash("Registro completado correctamente. Espere a que su cuenta sea asignada al personal correspondiente.", "success")
        return redirect(url_for("auth.login"))

    return render_register_form()

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        usuario = Usuario.query.filter_by(username=username).first()

        if usuario and check_password_hash(usuario.password, password):
            session["user_id"] = usuario.id
            session["username"] = usuario.username
            session["user_role"] = usuario.rol_id

            print(f"[DEBUG] Usuario {usuario.username}, rol: {usuario.rol_id}")

            if usuario.rol_id == 1:
                flash(f"Bienvenido, {usuario.username}.", "success")
                return redirect(url_for("admin.dashboard"))
            elif usuario.rol_id == 2:
                flash(f"Bienvenido, {usuario.username}.", "success")
                return redirect(url_for("director.dashboard"))
            elif usuario.rol_id == 3:
                flash(f"Bienvenido, {usuario.username}.", "success")
                return redirect(url_for("personal.dashboard"))
            else:
                flash("Rol desconocido.", "danger")
                return redirect(url_for("auth.login"))

        flash("Credenciales incorrectas. Intenta de nuevo.", "danger")

    return render_login_form()

@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("Has cerrado sesión correctamente.", "success")
    return redirect(url_for('home.index'))
