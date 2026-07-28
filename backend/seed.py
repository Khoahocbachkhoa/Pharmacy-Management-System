from app import create_app, db
from app.models import Medicine, Supplier

app = create_app()

with app.app_context():
    if Supplier.query.first():
        print("Đã có seed!")
        exit()

    suppliers = [
        Supplier(
            Name="Công ty Dược Bắc Ninh",
            Address="Bắc Ninh",
            Phone="02923891234"
        ),
        Supplier(
            Name="Công ty Traphaco",
            Address="Hà Nội",
            Phone="02437912345"
        ),
        Supplier(
            Name="Công ty Imexpharm",
            Address="Đồng Tháp",
            Phone="02773881234"
        ),
        Supplier(
            Name="Công ty Pymepharco",
            Address="Phú Yên",
            Phone="02573894567"
        ),
        Supplier(
            Name="Công ty Domesco",
            Address="Đồng Tháp",
            Phone="02773895678"
        )
    ]

    db.session.add_all(suppliers)
    db.session.commit()

    medicines = [
        Medicine(
            Name="Paracetamol 500mg",
            Category="Giảm đau - hạ sốt",
            Unit="Viên",
            Price=20000,
            Quantity=100,
            SupplierID=suppliers[0].SupplierID,
            Description="Giảm đau, hạ sốt"
        ),
        Medicine(
            Name="Alpha Choay",
            Category="Kháng viêm",
            Unit="Viên",
            Price=15000,
            Quantity=80,
            SupplierID=suppliers[1].SupplierID,
            Description="Chống phù nề"
        ),
        Medicine(
            Name="Vitamin C 500mg",
            Category="Vitamin",
            Unit="Viên",
            Price=15000,
            Quantity=120,
            SupplierID=suppliers[2].SupplierID,
            Description="Tăng sức đề kháng"
        ),
        Medicine(
            Name="Amoxicillin 500mg",
            Category="Kháng sinh",
            Unit="Viên",
            Price=40000,
            Quantity=60,
            SupplierID=suppliers[0].SupplierID,
            Description="Kháng sinh penicillin"
        ),
        Medicine(
            Name="Cefixime 200mg",
            Category="Kháng sinh",
            Unit="Viên",
            Price=60000,
            Quantity=50,
            SupplierID=suppliers[3].SupplierID,
            Description="Kháng sinh cephalosporin"
        ),
        Medicine(
            Name="Oresol",
            Category="Bù nước",
            Unit="Gói",
            Price=30000,
            Quantity=200,
            SupplierID=suppliers[4].SupplierID,
            Description="Bù nước và điện giải"
        ),
        Medicine(
            Name="Loratadine 10mg",
            Category="Chống dị ứng",
            Unit="Viên",
            Price=25000,
            Quantity=90,
            SupplierID=suppliers[1].SupplierID,
            Description="Chống dị ứng, viêm mũi"
        ),
        Medicine(
            Name="Smecta",
            Category="Tiêu hóa",
            Unit="Gói",
            Price=50000,
            Quantity=70,
            SupplierID=suppliers[2].SupplierID,
            Description="Điều trị tiêu chảy"
        ),
        Medicine(
            Name="Omeprazole 20mg",
            Category="Dạ dày",
            Unit="Viên",
            Price=45000,
            Quantity=65,
            SupplierID=suppliers[3].SupplierID,
            Description="Giảm tiết axit dạ dày"
        ),
        Medicine(
            Name="Salonpas",
            Category="Giảm đau ngoài da",
            Unit="Miếng",
            Price=8000,
            Quantity=40,
            SupplierID=suppliers[4].SupplierID,
            Description="Giảm đau cơ, khớp"
        ),
    ]

    db.session.add_all(medicines)
    db.session.commit()