"""First migration.

Revision ID: 78a710a40243
Revises: 
Create Date: 2018-11-27 23:42:28.787561

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78a710a40243'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('categoryname', sa.String(length=255), nullable=True),
    sa.Column('description', sa.Text(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_category_categoryname'), 'category', ['categoryname'], unique=True)
    op.create_table('customer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customername', sa.String(length=255), nullable=True),
    sa.Column('contactname', sa.String(length=255), nullable=True),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.Column('city', sa.String(length=255), nullable=True),
    sa.Column('postalcode', sa.String(length=255), nullable=True),
    sa.Column('country', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_customer_address'), 'customer', ['address'], unique=False)
    op.create_index(op.f('ix_customer_city'), 'customer', ['city'], unique=False)
    op.create_index(op.f('ix_customer_contactname'), 'customer', ['contactname'], unique=False)
    op.create_index(op.f('ix_customer_country'), 'customer', ['country'], unique=False)
    op.create_index(op.f('ix_customer_customername'), 'customer', ['customername'], unique=False)
    op.create_index(op.f('ix_customer_postalcode'), 'customer', ['postalcode'], unique=False)
    op.create_table('employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lastname', sa.String(length=255), nullable=True),
    sa.Column('firstname', sa.String(length=255), nullable=True),
    sa.Column('birthdate', sa.Date(), nullable=True),
    sa.Column('notes', sa.Text(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_employee_firstname'), 'employee', ['firstname'], unique=False)
    op.create_index(op.f('ix_employee_lastname'), 'employee', ['lastname'], unique=False)
    op.create_table('shipper',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('productname', sa.String(length=255), nullable=True),
    sa.Column('phone', sa.String(length=25), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_shipper_phone'), 'shipper', ['phone'], unique=False)
    op.create_index(op.f('ix_shipper_productname'), 'shipper', ['productname'], unique=False)
    op.create_table('supplier',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('suppliername', sa.String(length=255), nullable=True),
    sa.Column('contactname', sa.String(length=255), nullable=True),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.Column('city', sa.String(length=255), nullable=True),
    sa.Column('postalcode', sa.String(length=255), nullable=True),
    sa.Column('country', sa.String(length=255), nullable=True),
    sa.Column('phone', sa.String(length=25), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_supplier_address'), 'supplier', ['address'], unique=False)
    op.create_index(op.f('ix_supplier_city'), 'supplier', ['city'], unique=False)
    op.create_index(op.f('ix_supplier_contactname'), 'supplier', ['contactname'], unique=False)
    op.create_index(op.f('ix_supplier_country'), 'supplier', ['country'], unique=False)
    op.create_index(op.f('ix_supplier_phone'), 'supplier', ['phone'], unique=False)
    op.create_index(op.f('ix_supplier_postalcode'), 'supplier', ['postalcode'], unique=False)
    op.create_index(op.f('ix_supplier_suppliername'), 'supplier', ['suppliername'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('about_me', sa.String(length=255), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.Column('orderdate', sa.Date(), nullable=True),
    sa.Column('shipper_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], ),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.id'], ),
    sa.ForeignKeyConstraint(['shipper_id'], ['shipper.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post',
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_timestamp'), 'post', ['timestamp'], unique=False)
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('productname', sa.String(length=255), nullable=True),
    sa.Column('supplier_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('unit', sa.Integer(), nullable=True),
    sa.Column('price', sa.Numeric(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['supplier_id'], ['supplier.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_product_productname'), 'product', ['productname'], unique=False)
    op.create_table('order_detail',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_detail')
    op.drop_index(op.f('ix_product_productname'), table_name='product')
    op.drop_table('product')
    op.drop_index(op.f('ix_post_timestamp'), table_name='post')
    op.drop_table('post')
    op.drop_table('order')
    op.drop_table('followers')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_supplier_suppliername'), table_name='supplier')
    op.drop_index(op.f('ix_supplier_postalcode'), table_name='supplier')
    op.drop_index(op.f('ix_supplier_phone'), table_name='supplier')
    op.drop_index(op.f('ix_supplier_country'), table_name='supplier')
    op.drop_index(op.f('ix_supplier_contactname'), table_name='supplier')
    op.drop_index(op.f('ix_supplier_city'), table_name='supplier')
    op.drop_index(op.f('ix_supplier_address'), table_name='supplier')
    op.drop_table('supplier')
    op.drop_index(op.f('ix_shipper_productname'), table_name='shipper')
    op.drop_index(op.f('ix_shipper_phone'), table_name='shipper')
    op.drop_table('shipper')
    op.drop_index(op.f('ix_employee_lastname'), table_name='employee')
    op.drop_index(op.f('ix_employee_firstname'), table_name='employee')
    op.drop_table('employee')
    op.drop_index(op.f('ix_customer_postalcode'), table_name='customer')
    op.drop_index(op.f('ix_customer_customername'), table_name='customer')
    op.drop_index(op.f('ix_customer_country'), table_name='customer')
    op.drop_index(op.f('ix_customer_contactname'), table_name='customer')
    op.drop_index(op.f('ix_customer_city'), table_name='customer')
    op.drop_index(op.f('ix_customer_address'), table_name='customer')
    op.drop_table('customer')
    op.drop_index(op.f('ix_category_categoryname'), table_name='category')
    op.drop_table('category')
    # ### end Alembic commands ###
