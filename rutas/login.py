from flask import Blueprint, render_template
from database import get_db

login_bp = Blueprint('login', __name__, template_folder='templates/login')

@login_bp.route('/')
def login():
    return render_template('login/login.html')

