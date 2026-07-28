from flask import Blueprint, request, jsonify
from app.models import db, Invoice, InvoiceDetail, Medicine, Customer
from sqlalchemy import extract, func
from flask_jwt_extended import jwt_required

report_bp = Blueprint("report", __name__)

@report_bp.route("/api/report/sales/", methods=["GET"])
@jwt_required()
def get_sales_by_month():
    try:
        month = int(request.args.get("m"))
        year = int(request.args.get("y"))

        total = (
            db.session.query(func.sum(Invoice.TotalAmount))
            .filter(extract("month", Invoice.DateCreated) == month)
            .filter(extract("year", Invoice.DateCreated) == year)
            .scalar()
        )

        return jsonify({
            "month": month,
            "year": year,
            "total_sales": total or 0
        }), 200
    
    except Exception as e:
        return jsonify({"msg": str(e)}), 400

@report_bp.route("/api/report/invoices/", methods=["GET"])
@jwt_required()
def get_invoice_count_by_month():
    try:
        month = int(request.args.get("m"))
        year = int(request.args.get("y"))

        count = (
            db.session.query(func.count(Invoice.InvoiceID))
            .filter(extract("month", Invoice.DateCreated) == month)
            .filter(extract("year", Invoice.DateCreated) == year)
            .scalar()
        )

        return jsonify({
            "month": month,
            "year": year,
            "total_invoices": count
        }), 200

    except Exception as e:
        return jsonify({"msg": str(e)}), 400
    
@report_bp.route("/api/report/customers/", methods=["GET"])
@jwt_required()
def get_top_customers():
    try:
        month = int(request.args.get("m"))
        year = int(request.args.get("y"))

        results = (
            db.session.query(
                Customer.Name,
                func.sum(Invoice.TotalAmount).label("total_spent")
            )
            .join(Invoice, Invoice.CustomerID == Customer.CustomerID)
            .filter(extract("month", Invoice.DateCreated) == month)
            .filter(extract("year", Invoice.DateCreated) == year)
            .group_by(Customer.CustomerID)
            .order_by(func.sum(Invoice.TotalAmount).desc())
            .limit(5)
            .all()
        )

        data = [
            {
                "name": name,
                "total": total
            }
            for name, total in results
        ]

        return jsonify(data), 200

    except Exception as e:
        return jsonify({"msg": str(e)}), 400
    
@report_bp.route("/api/report/medicines/", methods=["GET"])
@jwt_required()
def get_report_medicines():
    try:
        month = int(request.args.get("m"))
        year = int(request.args.get("y"))

        query = (
            db.session.query(
                Medicine.Name,
                func.sum(InvoiceDetail.Quantity).label("total_sold")
            )
            .join(InvoiceDetail, Medicine.MedicineID == InvoiceDetail.MedicineID)
            .join(Invoice, Invoice.InvoiceID == InvoiceDetail.InvoiceID)
            .filter(extract("month", Invoice.DateCreated) == month)
            .filter(extract("year", Invoice.DateCreated) == year)
            .group_by(Medicine.MedicineID)
        )

        bestSellers = query.order_by(func.sum(InvoiceDetail.Quantity).desc()).limit(3).all()

        slowSellers = query.order_by(func.sum(InvoiceDetail.Quantity)).limit(3).all()

        return jsonify({
            "best_sellers": [
                {"name": name, "quantity": qty}
                for name, qty in bestSellers
            ],
            "slow_sellers": [
                {"name": name, "quantity": qty}
                for name, qty in slowSellers
            ]
        }), 200

    except Exception as e:
        return jsonify({"msg": str(e)}), 400