# Add Member App 👥

A modern desktop application for managing member information with a beautiful user interface built with Python.

[🇵🇸 نسخه فارسی](#نسخه-فارسی)

## 📋 Table of Contents

- [Features](#features)
- [Screenshots](#screenshots)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [License](#license)

## ✨ Features

- **Add Members**: Easily add new members with their personal information
- **Manage Information**: Store member details including:
  - First Name (نام)
  - Last Name (نام خانوادگی)
  - Gender (جنسیت)
  - Birth Date (تاریخ تولد) - Using Persian Shamsi Calendar
  - Photo (عکس)
- **View Members**: Display all members in a table format
- **Edit Members**: Update existing member information
- **Delete Members**: Remove members from the database
- **User-Friendly Interface**: Intuitive GUI with right-to-left support for Persian language
- **Photo Management**: Upload and store member photos in the database
- **Database Storage**: SQLite database for persistent data storage

## 📸 Screenshots

[Add screenshots here showing the application interface]

## 📦 Requirements

- Python 3.8 or higher
- tkinter (usually included with Python)
- customtkinter
- Pillow (PIL)
- shamsicalendar

## 🚀 Installation

### Step 1: Clone the repository
```bash
git clone https://github.com/yourusername/user_app.git
cd user_app
```

### Step 2: Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

Required packages:
```
customtkinter>=5.0
Pillow>=9.0
shamsicalendar>=1.0
```

### Step 4: Run the application
```bash
python app.py
```

## 💻 Usage

### Adding a Member
1. Click on "انتخاب عکس" (Select Photo) to choose a member's photo
2. Enter the member's first name in "نام" field
3. Enter the member's last name in "نام خانوادگی" field
4. Select gender from "جنسیت" dropdown (مرد/زن)
5. Select birth date using "تاریخ تولد" calendar (Persian date)
6. Click "اضافه کردن عضو" (Add Member) to save

### Viewing Members
- All members are displayed in the table at the bottom of the window
- You can scroll through the list to view all members

### Editing a Member
1. Right-click on a member in the table
2. Select "Edit" option
3. Modify the information as needed
4. Click "ویرایش کردن عضو" (Edit Member) to save changes

### Deleting a Member
1. Right-click on a member in the table
2. Select "Delete" to remove the member from the database

### Viewing Member Details
1. Right-click on a member in the table
2. Select "View" to see full member details including photo

## 📁 Project Structure

```
user_app/
├── app.py                    # Main application file with GUI
├── database_.py              # Database operations and connections
├── database_.sqlite3         # SQLite database file (created at runtime)
├── README.md                 # This file
└── requirements.txt          # Python dependencies
```

### File Descriptions

**app.py**
- Main application entry point
- Contains `App` class that handles GUI using CustomTkinter
- Manages user interactions (button clicks, form submissions)
- Implements context menu for table operations
- Window size: 650x500 pixels
- Supports Persian language interface

**database_.py**
- SQLite database connection and operations
- `connect()` - Establishes database connection
- `create_table()` - Creates persons table if not exists
- `add_member()` - Inserts new member record
- `show_members()` - Retrieves all members
- `delete_user_db()` - Deletes a member
- `update_user_db()` - Updates member information
- `convert_to_binary()` - Converts image files to binary for storage

## 🛠️ Technologies Used

- **Python 3** - Programming language
- **CustomTkinter** - Modern GUI toolkit for Python
- **SQLite3** - Lightweight database
- **Pillow (PIL)** - Image processing
- **ShamsiCalendar** - Persian date selection
- **tkinter** - Standard Python GUI library

## 🎨 UI Features

- **Modern Design**: Clean and intuitive interface with custom styling
- **RTL Support**: Right-to-left layout for Persian language
- **Color Scheme**: Professional gray and blue color palette
- **Responsive Layout**: Fixed window size for consistency
- **Table View**: Sortable column headers and scrollable data

## 🔒 Data Security

- Photos are stored as binary data in SQLite database
- Database constraints ensure data integrity (gender validation)
- Auto-increment IDs for unique member identification

## 📝 Database Schema

The application uses a single SQLite table with the following structure:

```sql
CREATE TABLE persons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    gender TEXT CHECK(gender IN ('زن', 'مرد')) NOT NULL,
    birthdate TEXT NOT NULL,
    photo BLOB
)
```

## 🐛 Troubleshooting

### Issue: Module not found errors
**Solution**: Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Issue: Database locked error
**Solution**: Close any other instances of the application and delete the `.sqlite3` file to reset the database.

### Issue: Photo not displaying
**Solution**: Ensure the image file format is supported by Pillow (JPG, PNG, etc.)

## 📈 Future Enhancements

- [ ] Export member list to CSV/PDF
- [ ] Search and filter functionality
- [ ] Advanced photo editing
- [ ] Member categories/groups
- [ ] Backup and restore database
- [ ] Email integration
- [ ] Multi-language support (add more languages)

## 👨‍💻 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Contact & Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

# نسخه فارسی

## اپلیکیشن مدیریت اعضا 👥

یک اپلیکیشن دسکتاپ مدرن برای مدیریت اطلاعات اعضا با رابط کاربری زیبا.

### ✨ ویژگی‌ها

- **افزودن اعضا**: اضافه کردن آسان اطلاعات شخصی اعضا
- **مدیریت اطلاعات**: ذخیره اطلاعات شامل:
  - نام
  - نام خانوادگی  
  - جنسیت
  - تاریخ تولد (با تقویم شمسی)
  - عکس
- **مشاهده اعضا**: نمایش تمام اعضا در جدول
- **ویرایش اعضا**: به‌روزرسانی اطلاعات اعضا
- **حذف اعضا**: حذف اعضا از پایگاه‌داده
- **رابط کاربری مناسب**: رابط شهودی با پشتیبانی جهت راست‌به‌چپ
- **مدیریت عکس**: آپلود و ذخیره عکس‌های اعضا
- **ذخیره‌سازی دائمی**: استفاده از پایگاه‌داده SQLite

### 🚀 نصب

#### مرحله 1: کلون کردن مخزن
```bash
git clone https://github.com/yourusername/user_app.git
cd user_app
```

#### مرحله 2: نصب وابستگی‌ها
```bash
pip install -r requirements.txt
```

#### مرحله 3: اجرای اپلیکیشن
```bash
python app.py
```

### 💻 نحوه استفاده

#### افزودن یک عضو
1. روی "انتخاب عکس" کلیک کنید
2. نام عضو را در قسمت "نام" وارد کنید
3. نام خانوادگی را در قسمت "نام خانوادگی" وارد کنید
4. جنسیت را از فهرست انتخاب کنید
5. تاریخ تولد را انتخاب کنید
6. روی "اضافه کردن عضو" کلیک کنید

#### ویرایش عضو
1. روی عضو مورد نظر در جدول راست‌کلیک کنید
2. گزینه "Edit" را انتخاب کنید
3. اطلاعات را تغییر دهید
4. روی "ویرایش کردن عضو" کلیک کنید

#### حذف عضو
1. روی عضو مورد نظر در جدول راست‌کلیک کنید
2. گزینه "Delete" را انتخاب کنید

### 🛠️ فناوری‌های استفاده‌شده

- **Python 3** - زبان برنامه‌نویسی
- **CustomTkinter** - کتابخانه رابط کاربری
- **SQLite3** - پایگاه‌داده سبک‌وزن
- **Pillow** - پردازش تصاویر
- **ShamsiCalendar** - تقویم شمسی
- **tkinter** - کتابخانه استاندارد GUI

---

**Created with ❤️ for Persian users**
