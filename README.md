# 🛒 Flask E-Commerce Web Application

A simple **E-Commerce web application** built with **Flask**, providing user authentication, product listings, cart management, and order checkout functionality.  

---

## ✨ Features  
- 🔑 **User Authentication** – Register, login, logout  
- 📦 **Product Management** – Browse, search, filter products  
- 🛍️ **Shopping Cart** – Add/remove products, update quantity  
- 💳 **Checkout System** – Place orders (dummy payment integration possible)  
- 📊 **Admin Dashboard** – Manage products & orders (optional)  
- 📱 **Responsive Design** – Works on desktop & mobile  

---

## ⚙️ Tech Stack  
- **Backend**: Flask (Python)  
- **Frontend**: HTML, CSS, Bootstrap / Tailwind  
- **Database**: SQLite / MySQL / PostgreSQL (choose one)  
- **Authentication**: Flask-Login / Flask-Security  
- **Deployment**: Gunicorn + Heroku / Render / AWS  

---

## 🚀 Installation & Setup  

1. **Clone the repository**  
```bash
git clone https://github.com/yourusername/flask-ecommerce.git
cd flask-ecommerce
```

2. **Create and activate a virtual environment**  
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate # On Mac/Linux
```

3. **Install dependencies**  
```bash
pip install -r requirements.txt
```

4. **Set up the database**  
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

5. **Run the application**  
```bash
flask run
```

6. Open in browser → [http://127.0.0.1:5000](http://127.0.0.1:5000)  

---

## 📂 Project Structure  
```
flask-ecommerce/
│── app/
│   ├── static/        # CSS, JS, Images
│   ├── templates/     # HTML templates
│   ├── models.py      # Database models
│   ├── routes.py      # Application routes
│   ├── forms.py       # Forms (login, register, etc.)
│   └── __init__.py    # App factory
│
│── migrations/        # Database migrations
│── requirements.txt   # Python dependencies
│── config.py          # Configuration file
│── run.py             # App entry point
│── README.md          # Project documentation
```

---

## 🧪 Future Enhancements  
- ✅ Payment Gateway Integration (Stripe / Razorpay / PayPal)  
- ✅ Product Categories & Search Filters  
- ✅ Admin Dashboard (Orders, Inventory)  
- ✅ Wishlist & Order History  

---

## 🤝 Contributing  
Contributions are welcome! Please fork the repo and submit a pull request.  

---

## 📜 License  
This project is licensed under the **MIT License** – free to use and modify.  
