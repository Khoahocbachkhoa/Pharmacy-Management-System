from flask import Blueprint, jsonify
from app.models import Medicine, Supplier
from flask_jwt_extended import jwt_required

common_bp = Blueprint('common', __name__)

@common_bp.route('/api/options/medicines', methods=['GET'])
@jwt_required()
def get_medicine_options():
    try:
        medicines = Medicine.query.all()
        
        result = [
            {
                "id": m.MedicineID,
                "name": m.Name,
                "unit": m.Unit,
                "price": m.Price
            } 
            for m in medicines
        ]

        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@common_bp.route('/api/options/suppliers', methods=['GET'])
@jwt_required()
def get_supplier_options():
    try:
        suppliers = Supplier.query.all()
        
        result = [
            {
                "id": s.SupplierID,
                "name": s.Name
            } 
            for s in suppliers
        ]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500