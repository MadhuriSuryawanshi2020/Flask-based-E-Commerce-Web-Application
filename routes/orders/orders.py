from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from db import db
from models import Product, Order, User

orders_bp = Blueprint("orders", __name__, template_folder="../../templates/orders")

# ✅ Browse products page (reuse for GET)
@orders_bp.route("/browse")
def browse():
    products = Product.query.all()
    return render_template("products/browse.html", products=products)

# ✅ Place order (only for customers)
# Customer places an order
@orders_bp.route("/place/<int:product_id>", methods=["POST"])
def place_order(product_id):
    if "user_id" not in session:
        flash("Please login to place order.")
        return redirect(url_for("users.login"))

    product = Product.query.get_or_404(product_id)
    user_id = session.get("user_id")

    if product.stock < 1:
        flash("Product out of stock.")
        return redirect(url_for("products.browse_products"))

    order = Order(user_id=user_id, product_id=product.id, quantity=1, status="Pending")
    db.session.add(order)
    product.stock -= 1
    db.session.commit()
    flash("Order placed successfully!")
    return redirect(url_for("products.browse_products"))

# Customer views **their own orders only** (status shown optionally)
@orders_bp.route("/my_orders")
def my_orders():
    if "user_id" not in session:
        flash("Please login to view orders.")
        return redirect(url_for("users.login"))

    user_id = session.get("user_id")
    orders = Order.query.filter_by(user_id=user_id).all()
    return render_template("my_orders.html", orders=orders)