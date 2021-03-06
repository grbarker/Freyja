"""Add back tables after altering them.

Revision ID: 9f614adf3ffa
Revises: 7180ba27f86a
Create Date: 2018-11-28 00:29:05.680512

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f614adf3ffa'
down_revision = '7180ba27f86a'
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
    sa.Column('birthdate', sa.DateTime(), nullable=True),
    sa.Column('notes', sa.Text(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_employee_firstname'), 'employee', ['firstname'], unique=False)
    op.create_index(op.f('ix_employee_lastname'), 'employee', ['lastname'], unique=False)
    op.create_table('shipper',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('shippername', sa.String(length=255), nullable=True),
    sa.Column('phone', sa.String(length=25), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_shipper_phone'), 'shipper', ['phone'], unique=False)
    op.create_index(op.f('ix_shipper_shippername'), 'shipper', ['shippername'], unique=False)
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
    op.drop_table('order')
    op.drop_index(op.f('ix_supplier_suppliername'), table_name='supplier')
    op.drop_index(op.f('ix_supplier_postalcode'), table_name='supplier')
    op.drop_index(op.f('ix_supplier_phone'), table_name='supplier')
    op.drop_index(op.f('ix_supplier_country'), table_name='supplier')
    op.drop_index(op.f('ix_supplier_contactname'), table_name='supplier')
    op.drop_index(op.f('ix_supplier_city'), table_name='supplier')
    op.drop_index(op.f('ix_supplier_address'), table_name='supplier')
    op.drop_table('supplier')
    op.drop_index(op.f('ix_shipper_shippername'), table_name='shipper')
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
