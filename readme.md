```text
+========================================================================+
| _____  _                                                               |
||  __ \| |                                                              |
|| |__) | |__   __ _ _ __ _ __ ___   __ _  ___ _   _    __ _ _ __  _ __  |
||  ___/| '_ \ / _` | '__| '_ ` _ \ / _` |/ __| | | |  / _` | '_ \| '_ \ |
|| |    | | | | (_| | |  | | | | | | (_| | (__| |_| | | (_| | |_) | |_) ||
||_|    |_| |_|\__,_|_|  |_| |_| |_|\__,_|\___|\__, |  \__,_| .__/| .__/ |
|                                               __/ |       | |   | |    |
|                                              |___/        |_|   |_|    |
+========================================================================+

# Pharmacy app
Ứng dụng quản lý tiệm thuốc đơn giản với các chức năng chính: 
    + quản lý kho
    + quản lý hóa đơn
    + quản lý khách hàng
    + thống kê báo cáo

Công nghệ sử dụng:
    FE: React + Vite
    BE: Flask + SQLite + Sqlalchemy

# Cách chạy ứng dụng

## Backend:
**Yêu cầu :** Python, pip

**Các bước:**
1. Điều hướng tới thư mục backend
2. Tạo môi trường ảo : `python -m venv venv`
3. Kích hoạt môi trường ảo: `venv\Scripts\activate` (Windows) hoặc `source venv/bin/activate` (Linux/Mac)
4. Cài các gói cần thiết : `pip install -r requirements.txt`
5. Khởi tạo server : `python run.py`
6. (Tùy chọn) Khởi tạo seed để hiển thị dữ liệu mẫu : `python seed.py`

## Frontend:
**Yêu cầu :** Node.js, npm

**Các bước:**
1. Điều hướng tới thư mục frontend
2. Cài các gói cần thiết : `npm install`
3. Khởi tạo ứng dụng : `npm run dev`