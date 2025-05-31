from flask import Blueprint, render_template
#from database import get_db

dashboard_bp = Blueprint('dashboard', __name__, template_folder='templates/dashboard')

@dashboard_bp.route('/')
def dashboard():
    #db = get_db()
    #dashboard = db.execute("SELECT * FROM usuarios").fetchall()
    return render_template('template/dashboard.html')

