# routes/users/users.py
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from db import db
from models import User

users_bp = Blueprint("users", __name__, template_folder="../../templates/users")

# ------------------ REGISTER ------------------
@users_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        phone = request.form["phone"]
        password = request.form["password"]

        # Check if username or email already exists
        if User.query.filter((User.username == username) | (User.email == email)).first():
            flash("Username or Email already exists.", "danger")
            return redirect(url_for("users.register"))

        # Create new user without password hashing
        new_user = User(username=username, email=email, phone=phone, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful! You can now login.", "success")
        return redirect(url_for("users.login"))

    return render_template("users/register.html")


# ------------------ LOGIN ------------------
@users_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Find user by username or email
        user = User.query.filter((User.username == username) | (User.email == username)).first()
        if user and user.password == password:
            session["user_id"] = user.id
            session["username"] = user.username
            flash(f"Welcome, {user.username}!", "success")

            # Redirect based on role (admin, seller, customer)
            if user.username == "admin":
                return redirect(url_for("admin.dashboard"))
            elif user.username == "seller":
                return redirect(url_for("products.seller_dashboard"))
            else:
                return redirect(url_for("products.browse_products"))
        else:
            flash("Invalid credentials.", "danger")
            return redirect(url_for("users.login"))

    return render_template("users/login.html")


# ------------------ LOGOUT ------------------
@users_bp.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully.", "info")
    return redirect(url_for("users.login"))
