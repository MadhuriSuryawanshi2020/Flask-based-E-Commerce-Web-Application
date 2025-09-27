from db import db

# ---------------------
# User model
# ---------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(256), nullable=False)

    # Relationship with orders
    orders = db.relationship('Order', back_populates='user')  # link to Order.user
    products = db.relationship("Product", backref="seller", lazy=True)  # Seller's products


# ---------------------
# Product model
# ---------------------
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    orders = db.relationship('Order', back_populates='product')

    # Link to seller
    seller_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


# ---------------------
# Order model
# ---------------------
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), nullable=False, default='Pending')  # New column

    # Relationship for easier access
    user = db.relationship('User', back_populates='orders')   # link back to User.orders
    product = db.relationship('Product', back_populates='orders')


    

