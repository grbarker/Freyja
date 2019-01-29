from app import create_app, db
from app.models import User, Post, Category, Employee, Order, OrderDetail, Product, Shipper, Supplier, Review

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Post': Post,
        'Category': Category,
        'Employee': Employee,
        'OrderDetail': OrderDetail,
        'Order': Order,
        'Product': Product,
        'Shipper': Shipper,
        'Supplier': Supplier,
        'Review': Review
        }