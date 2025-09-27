# Flask-Based E-Commerce Web Application

## Project Overview
This is a beginner-friendly **Flask-based e-commerce web application** with a simple and intuitive interface. It supports **user registration/login**, **product browsing**, **order placement**, and **role-based management** (Admin and Seller). Data is stored in **SQLite**, making it lightweight and easy to run locally. Bootstrap is used for responsive UI.

---

## Features

### **Customer**
- Register/Login
- Browse products
- Place orders
- View own orders (status: Pending / Delivered)

### **Seller**
- Login
- Add new products
- Edit/update product stock and price
- Delete products

### **Admin**
- Login
- Add/Edit/Delete users
- Add/Edit/Delete products
- View all orders, grouped by customer
- Update order status (Pending / Delivered)

---

## Database Schema (SQLite)

### **User Table**
| Column    | Type     | Description                 |
|-----------|---------|-----------------------------|
| id        | Integer | Primary key                 |
| username  | String  | Unique username             |
| email     | String  | Email address               |
| phone     | String  | Phone number                |
| password  | String  | Password (hashed)           |

### **Product Table**
| Column    | Type     | Description                       |
|-----------|---------|-----------------------------------|
| id        | Integer | Primary key                       |
| name      | String  | Product name                       |
| price     | Float   | Product price                      |
| stock     | Integer | Available stock                    |
| seller_id | Integer | Foreign key (User id of seller)   |

### **Order Table**
| Column     | Type     | Description                               |
|------------|---------|-------------------------------------------|
| id         | Integer | Primary key                               |
| user_id    | Integer | Foreign key to `User` (customer)         |
| product_id | Integer | Foreign key to `Product`                  |
| quantity   | Integer | Number of items ordered                    |
| status     | String  | Order status: Pending / Delivered         |

---

## Project Structure

E-Commerce-Web-App/
│
├─ app.py # Main Flask app
├─ db.py # Database instance
├─ models.py # SQLAlchemy models (User, Product, Order)
├─ routes/
│ ├─ users/
│ │ └─ users.py # Customer routes
│ ├─ products/
│ │ └─ products.py # Product routes
│ ├─ orders/
│ │ └─ orders.py # Order routes
│ └─ admin/
│ └─ admin.py # Admin routes
└─ seller/
│ └─ seller.py # Seller routes
├─ templates/
│ ├─ users/ # login.html, register.html
│ ├─ products/ # browse.html
│ ├─ admin/ # dashboard.html, add/edit product/user.html
│ └─ orders/ # my_orders.html
│ └─ seller/ # add_product.html, edit_product.html,seller_dashboard.html
├─ static/
│ ├─ css/
│ │ └─ style.css # Custom styling
└─ requirements.txt # Python dependencies

## Setup Instructions

1. **Clone the repository**
    git clone https://github.com/username/repo-name.git
    cd repo-name

2. Create a virtual environment
    python -m venv venv

3.  Activate the virtual environment
    Windows:venv\Scripts\activate
    Linux/macOS:source venv/bin/activate

4.  Install dependencies
    pip install -r requirements.txt

5.  Initialize the database

6.  Run the Flask app
    python app.py

7. Access the application
     Open browser: http://127.0.0.1:5000/

## Future Improvements
1.  Implement password hashing for security.
2.  Add pagination for products and orders.
3.  Allow product images upload and display.
4.  Implement search and filtering for products.
5.  Add email notifications for order updates.
6.  Implement roles using Flask-Login or Flask-Security instead of username checks.
7.  Support multiple sellers with seller dashboards.
8.  Add reporting dashboard for admin (sales, revenue, etc.).
