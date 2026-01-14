from flask import Blueprint, jsonify
from app.models import Medicine, Supplier
from flask_jwt_extended import jwt_required

# Lấy danh sách thuốc và các nhà cung cấp cho form nhập thuốc
common_bp = Blueprint('common', __name__)

# Đưa ra danh sách các loại thuốc
@common_bp.route('/api/options/medicines', methods=['GET'])
@jwt_required() # yêu cầu xác thực được người dùng để truy cập được  route
def get_medicine_options():
    try:
        # Lấy tất cả các loại thuốc trong cửa hàng
        # Khi số loại thuốc quá nhiều, nên dùng thay tìm kiếm!
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
        # Trả về kết quả
        return jsonify(result), 200
    except Exception as e:
        # Không thì báo lỗi
        return jsonify({"error": str(e)}), 500

# Đưa ra danh sách các nhà cung cấp
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