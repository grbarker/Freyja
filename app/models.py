import base64
import jwt
import os
from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5
from flask_login import UserMixin
from datetime import datetime
from app import db, login


##Pulled from https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-viii-followers
followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    customername = db.Column(db.String(255), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.String(255))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    address = db.Column(db.String(255), index=True)
    city = db.Column(db.String(255), index=True)
    postalcode = db.Column(db.String(255), index=True)
    country = db.Column(db.String(255), index=True)
    orders = db.relationship('Order', backref='customer', lazy='dynamic')
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    ##Pulled from https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-viii-followers
    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

    ##Next 3 pulled from https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-viii-followers
    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(
            followers.c.followed_id == user.id).count() > 0

    def followed_posts(self):
        followed = Post.query.join(
            followers, (followers.c.followed_id == Post.user_id)).filter(
                followers.c.follower_id == self.id)
        own = Post.query.filter_by(user_id=self.id)
        return followed.union(own).order_by(Post.timestamp.desc())


class Post(db.Model):
    body = db.Column(db.String(140))
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categoryname = db.Column(db.String(255), index=True, unique=True)
    description = db.Column(db.Text(500))
    products = db.relationship('Product', backref='category', lazy='dynamic')


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employeeID = db.Column(db.Integer, index=True, unique=True)
    password_hash = db.Column(db.String(128))
    lastname = db.Column(db.String(255), index=True)
    firstname = db.Column(db.String(255), index=True)
    notes = db.Column(db.Text(1000))

    def __repr__(self):
        return '<Employee {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    orderdate = db.Column(db.Date)
    shipper_id = db.Column(db.Integer, db.ForeignKey('shipper.id'))
    orderdetails = db.relationship('OrderDetail', backref='order', lazy='dynamic')


class OrderDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productname = db.Column(db.String(255), index=True)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    unit = db.Column(db.Integer)
    price = db.Column(db.Numeric())
    orderdetails = db.relationship('OrderDetail', backref='product', lazy='dynamic')


class Shipper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shippername = db.Column(db.String(255), index=True)
    phone = db.Column(db.String(25), index=True)
    orders = db.relationship('Order', backref='shipper', lazy='dynamic')


class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    suppliername = db.Column(db.String(255), index=True)
    contactname = db.Column(db.String(255), index=True)
    address = db.Column(db.String(255), index=True)
    city = db.Column(db.String(255), index=True)
    postalcode = db.Column(db.String(255), index=True)
    country = db.Column(db.String(255), index=True)
    phone = db.Column(db.String(25), index=True)
    products = db.relationship('Product', backref='supplier', lazy='dynamic')


@login.user_loader
def load_user(id):
    return User.query.get(int(id))