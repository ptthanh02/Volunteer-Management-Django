# 🌟 Hệ Thống Quản Lý Hoạt Động Tình Nguyện

![Project Banner](https://homepage.momocdn.net/img/momo-upload-api-220617165559-637910817596648573.jpg)

## 🚀 Tổng Quan Dự Án

Hệ Thống Quản Lý Hoạt Động Tình Nguyện là một ứng dụng web toàn diện được phát triển như là đồ án cuối kỳ cho môn học "Công Nghệ Mới Trong Phát Triển Ứng Dụng". Mục tiêu của chúng tôi là tạo ra một nền tảng trực quan để quản lý và theo dõi các hoạt động tình nguyện bằng Django.

### 🔗 Liên Kết
- **Demo Trực Tuyến:** [Hệ Thống Quản Lý Tình Nguyện](https://volunteer-management-django.onrender.com) (Có Thể Mất Vài Phút Để Khởi Động)

## 🔑 Thông Tin Đăng Nhập Để Kiểm Thử

### Quyền Quản Trị
- **Tên đăng nhập:** `admin`
- **Mật khẩu:** `123`

### Người Dùng Thông Thường
- **Tên đăng nhập:** `ptthanh02`
- **Mật khẩu:** `Tt123456`

## ✨ Tính Năng Chính

| Tính Năng | Mô Tả | Trạng Thái |
|---------|-------------|--------|
| 📅 Quản Lý Sự Kiện | Tạo, chỉnh sửa và theo dõi sự kiện tình nguyện | ✅ Đã Hoàn Thiện |
| 🔐 Xác Thực Người Dùng | Hệ thống đăng ký và đăng nhập an toàn | ✅ Đã Hoàn Thiện |
| 🤝 Tham Gia Sự Kiện | Đăng ký và đánh dấu sự kiện yêu thích dễ dàng | ✅ Đã Hoàn Thiện |
| 💸 Hệ Thống Quyên Góp | Hỗ trợ đóng góp tài chính cho sự kiện | ✅ Đã Hoàn Thiện |
| 📝 Báo Cáo Sự Kiện | Gửi và quản lý báo cáo sau sự kiện | ✅ Đã Hoàn Thiện |
| 🔍 Tìm Kiếm & Lọc | Tính năng khám phá sự kiện nâng cao | ✅ Đã Hoàn Thiện |
| 📊 Bảng Điều Khiển Cá Nhân | Quản lý thông tin và hoạt động cá nhân | ✅ Đã Hoàn Thiện |

## 🛠️ Hướng Dẫn Cài Đặt Ở Local

### Điều Kiện Tiên Quyết
- 🐍 Python 3.12+
- 🌐 Django 5.0.3+
- 💻 Hỗ Trợ Môi Trường Ảo

### Các Bước Cài Đặt

#### 1. Sao Chép Kho Mã Nguồn
```bash
git clone https://github.com/ptthanh02/Volunteer-Management-Django.git
cd Volunteer-Management-Django
```

#### 2. Tạo Môi Trường Ảo
```bash
# Trên macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Trên Windows
python -m venv venv
venv\Scripts\activate
```

#### 3. Cài Đặt Các Phụ Thuộc
```bash
pip install -r requirements.txt
```

#### 4. Thiết Lập Cơ Sở Dữ Liệu
```bash
# Tạo migration cho cơ sở dữ liệu
python manage.py makemigrations
python manage.py migrate

# Tạo tài khoản quản trị
python manage.py createsuperuser
```

#### 5. Chạy Máy Chủ Phát Triển
```bash
python manage.py runserver
```
🌐 Truy Cập: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## 🧪 Các Lệnh Hữu Ích

| Lệnh | Mô Tả |
|---------|-------------|
| `python manage.py test` | Chạy các bài kiểm tra của dự án |
| `python manage.py collectstatic` | Thu thập các tập tin tĩnh |
| `python manage.py flush` | Đặt lại cơ sở dữ liệu (sử dụng cẩn thận) |

---