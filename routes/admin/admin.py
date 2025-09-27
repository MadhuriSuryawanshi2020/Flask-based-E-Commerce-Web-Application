# routes/admin/admin.py
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from db import db
from models import User, Product, Order

admin_bp = Blueprint("admin", __name__, template_folder="../../templates/admin")

# ---------------- Admin Dashboard ----------------
@admin_bp.route("/dashboard")
def dashboard():
    if "user_id" not in session or session.get("username") != "admin":
        flash("Access denied. Admin only.", "danger")
        return redirect(url_for("users.login"))

    users = User.query.all()
    products = Product.query.all()
    orders = Order.query.order_by(Order.user_id).all()
    return render_template("admin/dashboard.html", users=users, products=products, orders=orders)

# ---------------- Users ----------------
@admin_bp.route("/add_user", methods=["GET", "POST"])
def add_user():
    if "user_id" not in session or session.get("username") != "admin":
        flash("Access denied.", "danger")
        return redirect(url_for("users.login"))

    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        phone = request.form["phone"]
        password = request.form["password"]

        if User.query.filter((User.username == username) | (User.email == email)).first():
            flash("Username or Email already exists.", "danger")
            return redirect(url_for("admin.add_user"))

        new_user = User(username=username, email=email, phone=phone, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash("User added successfully.", "success")
        return redirect(url_for("admin.dashboard"))

    return render_template("admin/add_user.html")

@admin_bp.route("/edit_user/<int:user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    if "user_id" not in session or session.get("username") != "admin":
        flash("Access denied.", "danger")
        return redirect(url_for("users.login"))

    user = User.query.get_or_404(user_id)
    if request.method == "POST":
        user.username = request.form["username"]
        user.email = request.form["email"]
        user.phone = request.form["phone"]
        if request.form.get("password"):
            user.password = request.form["password"]
        db.session.commit()
        flash("User updated successfully.", "success")
        return redirect(url_for("admin.dashboard"))

    return render_template("admin/edit_user.html", user=user)

@admin_bp.route("/delete_user/<int:user_id>")
def delete_user(user_id):
    if "user_id" not in session or session.get("username") != "admin":
        flash("Access denied.", "danger")
        return redirect(url_for("users.login"))

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash("User deleted successfully.", "success")
    return redirect(url_for("admin.dashboard"))

# ---------------- Products ----------------
@admin_bp.route("/add_product", methods=["GET", "POST"])
def add_product():
    if "user_id" not in session or session.get("username") != "admin":
        flash("Access denied.", "danger")
        return redirect(url_for("users.login"))

    if request.method == "POST":
        name = request.form["name"]
        price = float(request.form["price"])
        stock = int(request.form["stock"])

        new_product = Product(name=name, price=price, stock=stock, seller_id=1)  # admin as seller
        db.session.add(new_product)
        db.session.commit()
        flash("Product added successfully.", "success")
        return redirect(url_for("admin.dashboard"))

    return render_template("admin/add_product.html")

@admin_bp.route("/edit_product/<int:product_id>", methods=["GET", "POST"])
def edit_product(product_id):
    if "user_id" not in session or session.get("username") != "admin":
        flash("Access denied.", "danger")
        return redirect(url_for("users.login"))

    product = Product.query.get_or_404(product_id)
    if request.method == "POST":
        product.name = request.form["name"]
        product.price = float(request.form["price"])
        product.stock = int(request.form["stock"])
        db.session.commit()
        flash("Product updated successfully.", "success")
        return redirect(url_for("admin.dashboard"))

    return render_template("admin/edit_product.html", product=product)

@admin_bp.route("/delete_product/<int:product_id>")
def delete_product(product_id):
    if "user_id" not in session or session.get("username") != "admin":
        flash("Access denied.", "danger")
        return redirect(url_for("users.login"))

    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash("Product deleted successfully.", "success")
    return redirect(url_for("admin.dashboard"))

# ---------------- Orders ----------------
@admin_bp.route("/orders/update/<int:order_id>", methods=["POST"])
def update_order_status(order_id):
    if "user_id" not in session or session.get("username") != "admin":
        flash("Access denied.", "danger")
        return redirect(url_for("users.login"))

    order = Order.query.get_or_404(order_id)
    new_status = request.form.get("status")
    if new_status in ["Pending", "Delivered"]:
        order.status = new_status
        db.session.commit()
        flash(f"Order #{order.id} status updated to {new_status}", "success")
    return redirect(url_for("admin.dashboard"))
