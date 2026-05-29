# 📦 Inventory & Sales Management System

🔗 **Live Demo:** https://retail-inventory-system-6mjw.onrender.com

A full-featured Inventory & Sales Management Web Application built using **Flask, Pandas, and Matplotlib** with CSV-based storage.

This project simulates a real-world small business system where users can manage inventory, record sales, track revenue, and visualize analytics.

---

## 🚀 Features

### 🔐 Authentication System
- Login using CSV-based user storage
- Session-based authentication
- Route protection using `@before_request`
- Error handling for invalid credentials

### 📦 Inventory Management
- Add new products
- Track Product ID, Name, Category, Price, Quantity
- Inventory stored in `inventory.csv`

### 💰 Sales Management
- Record sales transactions
- Automatic stock deduction
- Auto-increment Sale ID
- Prevent negative stock
- Sales history tracking

### 📊 Dashboard & Analytics
- Total revenue calculation
- Revenue per product visualization
- Top 5 selling products
- Low stock alerts
- Charts generated using Matplotlib

### 🔎 Search Functionality
- Search products by name (case-insensitive)

---

## 🛠 Technologies Used

- **Python**
- **Flask**
- **Pandas**
- **Matplotlib**
- **HTML5**
- **CSS3**
- **CSV (File-based storage)**

---

## 📂 Project Structure
 Inventory-Management-System/
│
├── app.py
├── users.csv
├── inventory.csv
├── sales.csv
│
├── static/
│ ├── chart.png
│ ├── top_products.png
│
├── templates/
│ ├── login.html
│ ├── dashboard.html
│ ├── add_product.html
│ ├── record_sale.html
│ ├── low_stock.html
│ ├── search.html
│ ├── sales_history.html
│ └── top_products.html
│
└── README.md


---

## 🌟 How to Run Locally

```bash
pip install -r requirements.txt
python app.py

Then open:

http://127.0.0.1:5000
👩‍💻 Author

Muskan Shaikh

GitHub: https://github.com/Muskan2771
