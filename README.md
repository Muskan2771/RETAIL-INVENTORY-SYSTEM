# 📦 Inventory & Sales Management System

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

## ⚙ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2️⃣ Install Dependencies
pip install flask pandas matplotlib
3️⃣ Run the Application
python app.py

Open in browser:

http://127.0.0.1:5000/login
🔑 Default Login Credentials

Ensure users.csv contains:

username,password
admin,1234

Login with:

Username: admin
Password: 1234
🧠 How It Works

Flask handles routing and backend logic.

Pandas processes CSV data.

Inventory updates automatically when a sale is recorded.

Matplotlib generates business insight charts.

Sessions protect private routes.

Stock validation prevents over-selling.

📈 Business Logic Implemented

Prevent sale if stock is insufficient.

Automatically update inventory after sale.

Generate unique Sale IDs.

Group and aggregate sales data for analytics.

Identify low-stock products dynamically.

⚠ Limitations

CSV storage is not scalable for large data.

No password hashing (for demo purposes).

No concurrency handling.

Not optimized for production deployment.

🚀 Future Improvements

Replace CSV with MySQL/PostgreSQL

Implement password hashing (bcrypt)

Add product edit/delete functionality

Add sales edit/delete functionality

Convert to REST API architecture

Add role-based access control

Deploy using Docker & cloud services

👩‍💻 Author

Muskan
Python Developer | Data Analytics Enthusiast

📄 License

This project is built for educational and demonstration purposes.


---

# 🔥 Before Uploading to GitHub

1. Create `README.md`
2. Paste above content
3. Replace:

your-username
your-repo-name

4. Push to GitHub

---

If you want, I can also give:

- ⭐ Short GitHub description (one-line)
- 💼 Resume-ready 3 bullet points
- 🏢 MNC-level project explanation
- 📊 Architecture diagram explanation

Tell me what you want next 😎
