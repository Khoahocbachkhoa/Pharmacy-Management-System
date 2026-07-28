from flask import Blueprint, request, jsonify
from app.models import db, Customer
from flask_jwt_extended import jwt_required

customer_bp = Blueprint('customer', __name__)

@customer_bp.route('/api/customers', methods=['GET'])
@jwt_required()
def get_customers():
    try:
        customers = Customer.query.all()

        results = [{
            "id": c.CustomerID,
            "name": c.Name,
            "phone": c.Phone,
            "address": c.Address
        } for c in customers]
        return jsonify(results), 200
    except Exception as e:
        return jsonify({"msg": str(e)}), 500

@customer_bp.route('/api/customers', methods=['POST'])
@jwt_required()
def add_customer():
    try:
        data = request.get_json()
        if not data.get('name'):
            return jsonify({"msg": "Lỗi không có tên khách hàng"}), 400

        new_customer = Customer(
            Name=data.get('name'),
            Phone=data.get('phone'),
            Address=data.get('address')
        )

        db.session.add(new_customer)
        db.session.commit()
        return jsonify({"msg": "Thêm khách hàng thành công", "id": new_customer.CustomerID}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": str(e)}), 500

@customer_bp.route('/api/customers/search', methods=['GET'])
@jwt_required()
def search_customers():
    try:
        query_text = request.args.get('q', '').strip()
        if not query_text:
            return jsonify([]), 200

        customers = Customer.query.filter(
            (Customer.Name.ilike(f"%{query_text}%")) | 
            (Customer.Phone.ilike(f"%{query_text}%"))
        ).all()

        data = [{
            "id": c.CustomerID,
            "name": c.Name,
            "phone": c.Phone,
            "address": c.Address
        } for c in customers]

        return jsonify(data), 200
    except Exception as e:
        return jsonify({"msg": str(e)}), 500