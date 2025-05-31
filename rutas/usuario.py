from flask import Blueprint, render_template
from database import get_db

usuarios_bp = Blueprint('usuarios', __name__, template_folder='templates/usuarios')

@usuarios_bp.route('/')
def lista_usuarios():
    db = get_db()
    usuarios = db.execute("SELECT * FROM usuarios").fetchall()
    return render_template('usuarios/lista.html')

@usuarios_bp.route('/perfil/<username>')
def perfil_usuario(username):
    return render_template('usuarios/perfil.html', username=username)
