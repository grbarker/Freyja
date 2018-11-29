from app import app, db
from app.models import User, Post, Category, Employee, Shipper, Supplier

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Category': Category, 'Employee': Employee, 'Shipper': Shipper, 'Supplier': Supplier}