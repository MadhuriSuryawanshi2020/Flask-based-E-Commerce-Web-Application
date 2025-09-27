from flask import Flask
from db import db
from sqlalchemy import event
from sqlalchemy.engine import Engine
import sqlite3

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, sqlite3.Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()


def create_app():
    app = Flask(__name__)
    app.secret_key = "secretkey"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        from models import User, Product, Order
        db.create_all()

    # Register blueprints
    from routes.users.users import users_bp
    from routes.products.products import products_bp
    from routes.orders.orders import orders_bp
    from routes.admin.admin import admin_bp
    from routes.seller.seller import seller_bp
   

    app.register_blueprint(users_bp, url_prefix="/users")
    app.register_blueprint(products_bp, url_prefix="/products")
    app.register_blueprint(orders_bp, url_prefix="/orders")
    app.register_blueprint(admin_bp, url_prefix="/admin")
    app.register_blueprint(seller_bp, url_prefix="/seller")


    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
