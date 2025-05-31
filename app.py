from dulwich.web import url_prefix
from flask import Flask
from rutas.home import home_bp
from rutas.usuario import usuarios_bp
from rutas.dashboard import dashboard_bp

from database import create_tables

app = Flask(__name__)

app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
app.register_blueprint(home_bp, url_prefix='/home')
app.register_blueprint(usuarios_bp, url_prefix='/usuarios')


if __name__ == '__main__':
    create_tables()
    app.run(debug=True)