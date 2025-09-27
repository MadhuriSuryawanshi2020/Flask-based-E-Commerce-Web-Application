from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from db import db
from models import Product, User

seller_bp = Blueprint("seller", __name__, template_folder="../../templates/seller")

# ✅ Seller Dashboard
@seller_bp.route("/dashboard")
def dashboard():
    if "user_id" not in session or session.get("username") == "admin":
        flash("Access denied. Seller only.")
        return redirect(url_for("users.login"))

    seller_id = session["user_id"]
    products = Product.query.filter_by(seller_id=seller_id).all()
    return render_template("seller/seller_dashboard.html", products=products)

# ✅ Add Product
@seller_bp.route("/add_product", methods=["GET", "POST"])
def add_product():
    if "user_id" not in session or session.get("username") == "admin":
        flash("Access denied. Seller only.")
        return redirect(url_for("users.login"))

    if request.method == "POST":
        name = request.form["name"]
        price = float(request.form["price"])
        stock = int(request.form["stock"])

        new_product = Product(
            name=name,
            price=price,
            stock=stock,
            seller_id=session["user_id"]
        )
        db.session.add(new_product)
        db.session.commit()
        flash("Product added successfully.")
        return redirect(url_for("seller.dashboard"))

    return render_template("seller/add_product.html")

# ✅ Edit Product
@seller_bp.route("/edit_product/<int:product_id>", methods=["GET", "POST"])
def edit_product(product_id):
    if "user_id" not in session or session.get("username") == "admin":
        flash("Access denied. Seller only.")
        return redirect(url_for("users.login"))

    product = Product.query.get_or_404(product_id)
    if product.seller_id != session["user_id"]:
        flash("You cannot edit this product.")
        return redirect(url_for("seller.dashboard"))

    if request.method == "POST":
        product.name = request.form["name"]
        product.price = float(request.form["price"])
        product.stock = int(request.form["stock"])
        db.session.commit()
        flash("Product updated successfully.")
        return redirect(url_for("seller.dashboard"))

    return render_template("seller/edit_product.html", product=product)

# ✅ Delete Product
@seller_bp.route("/delete_product/<int:product_id>")
def delete_product(product_id):
    if "user_id" not in session or session.get("username") == "admin":
        flash("Access denied. Seller only.")
        return redirect(url_for("users.login"))

    product = Product.query.get_or_404(product_id)
    if product.seller_id != session["user_id"]:
        flash("You cannot delete this product.")
        return redirect(url_for("seller.dashboard"))

    db.session.delete(product)
    db.session.commit()
    flash("Product deleted successfully.")
    return redirect(url_for("seller.dashboard"))
