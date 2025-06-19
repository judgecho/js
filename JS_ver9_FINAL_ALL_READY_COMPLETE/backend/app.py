from flask import Flask
from flask_cors import CORS
from models import db
from statistics import stats_bp

app = Flask(__name__)
from admin import admin_bp
app.register_blueprint(admin_bp)
from export_excel import excel_bp
app.register_blueprint(excel_bp)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
CORS(app)

db.init_app(app)
app.register_blueprint(stats_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)