from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from db import db
from models import Product, User

products_bp = Blueprint("products", __name__, template_folder="../../templates/products")

@products_bp.route("/browse")
def browse_products():
    products = Product.query.all()
    return render_template("browse.html", products=products)

@products_bp.route("/dashboard")
def seller_dashboard():
    user_id = session.get("user_id")
    if not user_id:
        flash("Please login first!", "danger")
        return redirect(url_for("users.login"))

    user = User.query.get(user_id)
    if user.username != "seller" and user.username != "admin":
        flash("Access denied!", "danger")
        return redirect(url_for("products.browse"))

    products = Product.query.all() if user.username=="admin" else Product.query.filter_by(seller_id=user.id).all()
    return render_template("seller_dashboard.html", products=products)

@products_bp.route("/add", methods=["GET", "POST"])
def add_product():
    user_id = session.get("user_id")
    if not user_id:
        flash("Please login first!", "danger")
        return redirect(url_for("users.login"))

    user = User.query.get(user_id)
    if user.username != "seller" and user.username != "admin":
        flash("Access denied!", "danger")
        return redirect(url_for("products.browse_products"))

    if request.method=="POST":
        name = request.form["name"]
        price = float(request.form["price"])
        stock = int(request.form["stock"])
        product = Product(name=name, price=price, stock=stock, seller_id=user.id)
        db.session.add(product)
        db.session.commit()
        flash("Product added successfully!", "success")
        return redirect(url_for("products.seller_dashboard"))

    return render_template("add_product.html")

@products_bp.route("/update/<int:product_id>", methods=["GET","POST"])
def update_product(product_id):
    user_id = session.get("user_id")
    if not user_id:
        flash("Login required!", "danger")
        return redirect(url_for("users.login"))

    product = Product.query.get_or_404(product_id)
    user = User.query.get(user_id)

    if user.username!="admin" and product.seller_id != user.id:
        flash("Not allowed!", "danger")
        return redirect(url_for("products.browse_products"))

    if request.method=="POST":
        product.name = request.form["name"]
        product.price = float(request.form["price"])
        product.stock = int(request.form["stock"])
        db.session.commit()
        flash("Product updated!", "success")
        return redirect(url_for("products.seller_dashboard"))

    return render_template("add_product.html", product=product)

@products_bp.route("/delete/<int:product_id>")
def delete_product(product_id):
    user_id = session.get("user_id")
    if not user_id:
        flash("Login required!", "danger")
        return redirect(url_for("users.login"))

    product = Product.query.get_or_404(product_id)
    user = User.query.get(user_id)

    if user.username!="admin" and product.seller_id != user.id:
        flash("Not allowed!", "danger")
        return redirect(url_for("products.browse_products"))

    db.session.delete(product)
    db.session.commit()
    flash("Product deleted!", "success")
    return redirect(url_for("products.seller_dashboard"))
