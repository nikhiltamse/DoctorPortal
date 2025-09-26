import os
from flask import Flask, send_from_directory
from src.models.user import db, User
from src.models.appointment import Appointment
from src.models.prescription import Prescription
from src.routes.user import user_bp
from src.routes.appointment import appointment_bp
from src.routes.prescription import prescription_bp
from src.routes.auth import auth_bp
from src.routes.templates import templates_bp
from src.routes.pdf import pdf_bp

# Create Flask app
app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "asdf#FGSgvasgf$5$WGT")

# Database config (SQLite fallback if DATABASE_URL not provided)
db_path = os.path.join(os.path.dirname(__file__), "database", "app.db")
os.makedirs(os.path.dirname(db_path), exist_ok=True)  # Ensure folder exists
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", f"sqlite:///{db_path}")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

with app.app_context():
    db.create_all()

# Register Blueprints
app.register_blueprint(user_bp, url_prefix="/api/users")
app.register_blueprint(appointment_bp, url_prefix="/api/appointments")
app.register_blueprint(prescription_bp, url_prefix="/api/prescriptions")
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(templates_bp, url_prefix="/api/templates")
app.register_blueprint(pdf_bp, url_prefix="/api/pdf")

# Default root route
@app.route("/")
def index():
    return {"message": "Flask app is running 🚀"}

# Static file handler
@app.route("/<path:path>")
def serve_static(path):
    if path and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    elif os.path.exists(os.path.join(app.static_folder, "index.html")):
        return send_from_directory(app.static_folder, "index.html")
    else:
        return "File not found", 404

# Run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=True)
