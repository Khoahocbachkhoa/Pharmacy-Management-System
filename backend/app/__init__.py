import os
from flask import Flask
from flask_cors import CORS
from .models import db
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

jwt = JWTManager()

def create_app():
    load_dotenv()
    
    app = Flask(__name__)
    CORS(app)

    # Cấu hình đường dẫn DB
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(BASE_DIR, "../database.db")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Cấu hình JWT
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

    # Khởi tạo DB với App
    db.init_app(app)
    # Khởi tạo JWT
    jwt.init_app(app)

    # Đăng ký các Routes (Blueprint)
    from app.routes.login import login_bp
    from app.routes.common import common_bp
    from app.routes.import_stock import import_bp
    from app.routes.medicine import medicine_bp
    from app.routes.customer import customer_bp
    from app.routes.invoice import invoice_bp
    from app.routes.report import report_bp
    
    app.register_blueprint(login_bp)
    app.register_blueprint(common_bp)
    app.register_blueprint(import_bp)
    app.register_blueprint(medicine_bp)
    app.register_blueprint(customer_bp)
    app.register_blueprint(invoice_bp)
    app.register_blueprint(report_bp)

    # Tạo bảng trong Database
    with app.app_context():
        db.create_all()

    return app