import os
from flask import Flask, render_template, request, url_for, redirect, session
import pandas as pd
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt

app = Flask(__name__)
app.secret_key = "your_super_secret_key"

# ------------------------------
# LOGIN ROUTE
# ------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()

        df_users = pd.read_csv('users.csv')

        df_users['username'] = df_users['username'].astype(str).str.strip()
        df_users['password'] = df_users['password'].astype(str).str.strip()

        user = df_users[
            (df_users['username'] == username) &
            (df_users['password'] == password)
        ]

        if not user.empty:
            session['username'] = username
            return redirect('/dashboard')
        else:
            error = "Wrong username or password!"

    return render_template('login.html', error=error)

# ------------------------------
# LOGOUT
# ------------------------------
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')


# ------------------------------
# PROTECT ROUTES
# ------------------------------
@app.before_request
def require_login():
    allowed_routes = ['login', 'static']

    if request.endpoint not in allowed_routes and 'username' not in session:
        return redirect('/login')


# ------------------------------
# HOME
# ------------------------------
@app.route('/')
def home():
    return redirect('/login')


# ------------------------------
# DASHBOARD
# ------------------------------
@app.route('/dashboard')
def dashboard():
    df_sales = pd.read_csv('sales.csv')
    df_inventory = pd.read_csv('inventory.csv')

    # Revenue per product
    revenue_per_product = df_sales.groupby('ProductName')['Total'].sum()

    plt.figure(figsize=(6, 4))
    revenue_per_product.plot(kind='bar')
    plt.title('Revenue per Product')
    plt.ylabel('Revenue')
    plt.tight_layout()

    chart_path = os.path.join('static', 'chart.png')
    plt.savefig(chart_path)
    plt.close()

    total_revenue = df_sales['Total'].sum()

    threshold = 5
    low_stock_count = df_inventory[df_inventory['Quantity'] < threshold].shape[0]

    return render_template(
        'dashboard.html',
        chart=url_for('static', filename='chart.png'),
        total_revenue=total_revenue,
        low_stock_count=low_stock_count
    )


# ------------------------------
# TOP 5 PRODUCTS
# ------------------------------
@app.route('/top-products')
def top_products():
    df_sales = pd.read_csv('sales.csv')

    top5 = (
        df_sales.groupby('ProductName')['Quantity']
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    plt.figure(figsize=(6, 4))
    top5.plot(kind='bar')
    plt.title('Top 5 Selling Products')
    plt.ylabel('Quantity Sold')
    plt.tight_layout()

    chart_path = os.path.join('static', 'top_products.png')
    plt.savefig(chart_path)
    plt.close()

    return render_template(
        'top_products.html',
        chart=url_for('static', filename='top_products.png')
    )


# ------------------------------
# LOW STOCK
# ------------------------------
@app.route('/low_stock')
def low_stock():
    df_inventory = pd.read_csv('inventory.csv')

    threshold = 5
    low_items = df_inventory[df_inventory['Quantity'] < threshold]

    return render_template(
        'low_stock.html',
        items=low_items.to_dict(orient='records')
    )


# ------------------------------
# SEARCH
# ------------------------------
@app.route('/search')
def search():
    query = request.args.get('query', '')

    df = pd.read_csv('inventory.csv')
    filtered = df[
        df['ProductName'].str.contains(query, case=False, na=False)
    ]

    return render_template(
        'search.html',
        items=filtered.to_dict(orient='records')
    )


# ------------------------------
# SALES HISTORY
# ------------------------------
@app.route('/sales-history')
def sales_history():
    df_sales = pd.read_csv('sales.csv')

    df_sales = df_sales.sort_values(by='Date', ascending=False)

    return render_template(
        'sales_history.html',
        sales=df_sales.to_dict(orient='records')
    )


# ------------------------------
# ADD PRODUCT
# ------------------------------
@app.route('/add-product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        product_id = request.form['product_id']
        name = request.form['name']
        category = request.form['category']
        price = float(request.form['price'])
        quantity = int(request.form['quantity'])

        df = pd.read_csv('inventory.csv')

        new_row = pd.DataFrame([{
            'ProductID': product_id,
            'ProductName': name,
            'Category': category,
            'Price': price,
            'Quantity': quantity
        }])

        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv('inventory.csv', index=False)

        return redirect('/dashboard')

    return render_template('add_product.html')


# ------------------------------
# RECORD SALE
# ------------------------------
@app.route('/record-sale', methods=['GET', 'POST'])
def record_sale():
    if request.method == 'POST':
        product_id = int(request.form['product_id'])
        quantity_sold = int(request.form['quantity'])
        date = request.form['date']

        df_inventory = pd.read_csv('inventory.csv')

        product = df_inventory[df_inventory['ProductID'] == product_id]

        if product.empty:
            return "Product ID not found!"

        current_quantity = int(product.iloc[0]['Quantity'])

        if quantity_sold > current_quantity:
            return "Not enough stock available!"

        product_name = product.iloc[0]['ProductName']
        price = float(product.iloc[0]['Price'])
        total = price * quantity_sold

        df_inventory.loc[
            df_inventory['ProductID'] == product_id,
            'Quantity'
        ] -= quantity_sold

        df_inventory.to_csv('inventory.csv', index=False)

        df_sales = pd.read_csv('sales.csv')

        sale_id = 1 if df_sales.empty else df_sales['SaleID'].max() + 1

        new_sale = pd.DataFrame([{
            'SaleID': sale_id,
            'ProductID': product_id,
            'ProductName': product_name,
            'Quantity': quantity_sold,
            'Total': total,
            'Date': date
        }])

        df_sales = pd.concat([df_sales, new_sale], ignore_index=True)
        df_sales.to_csv('sales.csv', index=False)

        return redirect('/dashboard')

    # 🔥 SEND PRODUCTS TO TEMPLATE
    df_inventory = pd.read_csv('inventory.csv')
    return render_template(
        'record_sale.html',
        products=df_inventory.to_dict(orient='records')
    )
# ------------------------------
# RUN APP
# ------------------------------
if __name__ == '__main__':
    app.run(debug=True)