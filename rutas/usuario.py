from flask import Blueprint

usuarios_dp = Blueprint('usuarios', __name__)

@usuarios_dp.route('/')
def usuarios():
    return 'Bienvenido a Usuarios'

@usuarios_dp.route('/perfil/<username>')
def perfil_usuario(username):
    return f'perfil de {username}'
