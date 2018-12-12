"""Remove tables to edit a column in Product table. Edit will add precision and scale parameters to Numeric data type.

Revision ID: a5fd08db3e3f
Revises: 5a099a3dde86
Create Date: 2018-12-10 13:40:23.094447

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5fd08db3e3f'
down_revision = '5a099a3dde86'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_shipper_phone', table_name='shipper')
    op.drop_index('ix_shipper_shippername', table_name='shipper')
    op.drop_table('shipper')
    op.drop_index('ix_product_productname', table_name='product')
    op.drop_table('product')
    op.drop_table('order_detail')
    op.drop_index('ix_user_address', table_name='user')
    op.drop_index('ix_user_city', table_name='user')
    op.drop_index('ix_user_country', table_name='user')
    op.drop_index('ix_user_customername', table_name='user')
    op.drop_index('ix_user_email', table_name='user')
    op.drop_index('ix_user_firstname', table_name='user')
    op.drop_index('ix_user_lastname', table_name='user')
    op.drop_index('ix_user_postalcode', table_name='user')
    op.drop_index('ix_user_username', table_name='user')
    op.drop_table('user')
    op.drop_index('ix_category_categoryname', table_name='category')
    op.drop_table('category')
    op.drop_index('ix_employee_employeeID', table_name='employee')
    op.drop_index('ix_employee_firstname', table_name='employee')
    op.drop_index('ix_employee_lastname', table_name='employee')
    op.drop_table('employee')
    op.drop_index('ix_supplier_address', table_name='supplier')
    op.drop_index('ix_supplier_city', table_name='supplier')
    op.drop_index('ix_supplier_contactname', table_name='supplier')
    op.drop_index('ix_supplier_country', table_name='supplier')
    op.drop_index('ix_supplier_phone', table_name='supplier')
    op.drop_index('ix_supplier_postalcode', table_name='supplier')
    op.drop_index('ix_supplier_suppliername', table_name='supplier')
    op.drop_table('supplier')
    op.drop_table('followers')
    op.drop_index('ix_post_timestamp', table_name='post')
    op.drop_table('post')
    op.drop_table('order')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('orderdate', sa.DATE(), nullable=True),
    sa.Column('shipper_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['shipper_id'], ['shipper.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post',
    sa.Column('body', sa.VARCHAR(length=140), nullable=True),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_post_timestamp', 'post', ['timestamp'], unique=False)
    op.create_table('followers',
    sa.Column('follower_id', sa.INTEGER(), nullable=True),
    sa.Column('followed_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    op.create_table('supplier',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('suppliername', sa.VARCHAR(length=255), nullable=True),
    sa.Column('contactname', sa.VARCHAR(length=255), nullable=True),
    sa.Column('address', sa.VARCHAR(length=255), nullable=True),
    sa.Column('city', sa.VARCHAR(length=255), nullable=True),
    sa.Column('postalcode', sa.VARCHAR(length=255), nullable=True),
    sa.Column('country', sa.VARCHAR(length=255), nullable=True),
    sa.Column('phone', sa.VARCHAR(length=25), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_supplier_suppliername', 'supplier', ['suppliername'], unique=False)
    op.create_index('ix_supplier_postalcode', 'supplier', ['postalcode'], unique=False)
    op.create_index('ix_supplier_phone', 'supplier', ['phone'], unique=False)
    op.create_index('ix_supplier_country', 'supplier', ['country'], unique=False)
    op.create_index('ix_supplier_contactname', 'supplier', ['contactname'], unique=False)
    op.create_index('ix_supplier_city', 'supplier', ['city'], unique=False)
    op.create_index('ix_supplier_address', 'supplier', ['address'], unique=False)
    op.create_table('employee',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('employeeID', sa.INTEGER(), nullable=True),
    sa.Column('password_hash', sa.VARCHAR(length=128), nullable=True),
    sa.Column('lastname', sa.VARCHAR(length=255), nullable=True),
    sa.Column('firstname', sa.VARCHAR(length=255), nullable=True),
    sa.Column('notes', sa.TEXT(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_employee_lastname', 'employee', ['lastname'], unique=False)
    op.create_index('ix_employee_firstname', 'employee', ['firstname'], unique=False)
    op.create_index('ix_employee_employeeID', 'employee', ['employeeID'], unique=1)
    op.create_table('category',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('categoryname', sa.VARCHAR(length=255), nullable=True),
    sa.Column('description', sa.TEXT(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_category_categoryname', 'category', ['categoryname'], unique=1)
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), nullable=True),
    sa.Column('customername', sa.VARCHAR(length=255), nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), nullable=True),
    sa.Column('password_hash', sa.VARCHAR(length=128), nullable=True),
    sa.Column('about_me', sa.VARCHAR(length=255), nullable=True),
    sa.Column('last_seen', sa.DATETIME(), nullable=True),
    sa.Column('address', sa.VARCHAR(length=255), nullable=True),
    sa.Column('city', sa.VARCHAR(length=255), nullable=True),
    sa.Column('postalcode', sa.VARCHAR(length=255), nullable=True),
    sa.Column('country', sa.VARCHAR(length=255), nullable=True),
    sa.Column('firstname', sa.VARCHAR(length=255), nullable=True),
    sa.Column('lastname', sa.VARCHAR(length=255), nullable=True),
    sa.Column('middlename', sa.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_user_username', 'user', ['username'], unique=1)
    op.create_index('ix_user_postalcode', 'user', ['postalcode'], unique=False)
    op.create_index('ix_user_lastname', 'user', ['lastname'], unique=False)
    op.create_index('ix_user_firstname', 'user', ['firstname'], unique=False)
    op.create_index('ix_user_email', 'user', ['email'], unique=1)
    op.create_index('ix_user_customername', 'user', ['customername'], unique=False)
    op.create_index('ix_user_country', 'user', ['country'], unique=False)
    op.create_index('ix_user_city', 'user', ['city'], unique=False)
    op.create_index('ix_user_address', 'user', ['address'], unique=False)
    op.create_table('order_detail',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('order_id', sa.INTEGER(), nullable=True),
    sa.Column('product_id', sa.INTEGER(), nullable=True),
    sa.Column('quantity', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('productname', sa.VARCHAR(length=255), nullable=True),
    sa.Column('supplier_id', sa.INTEGER(), nullable=True),
    sa.Column('category_id', sa.INTEGER(), nullable=True),
    sa.Column('unit', sa.INTEGER(), nullable=True),
    sa.Column('price', sa.NUMERIC(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['supplier_id'], ['supplier.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_product_productname', 'product', ['productname'], unique=False)
    op.create_table('shipper',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('shippername', sa.VARCHAR(length=255), nullable=True),
    sa.Column('phone', sa.VARCHAR(length=25), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_shipper_shippername', 'shipper', ['shippername'], unique=False)
    op.create_index('ix_shipper_phone', 'shipper', ['phone'], unique=False)
    # ### end Alembic commands ###