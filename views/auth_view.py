from flask import render_template

def render_login_form():
    """Renderiza el formulario de inicio de sesión."""
    return render_template("auth/login.html")

def render_register_form():
    """Renderiza el formulario de registro."""
    return render_template("auth/register.html")
