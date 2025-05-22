from flask import Blueprint, render_template
from database import get_db

home_bp = Blueprint('home', __name__, template_folder='templates')

@home_bp.route('/')
def home():
    return 'bienvenido a la pagina principal'

