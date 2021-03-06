import base64
import jwt
import os
from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5
from flask import current_app, url_for
from flask_login import UserMixin
from datetime import datetime
from time import time
from app import db, login
from app.search import add_to_index, remove_from_index, query_index


class SearchableMixin(object):
    @classmethod
    def search(cls, expression, page, per_page):
        ids, total = query_index(cls.__tablename__, expression, page, per_page)
        if total == 0:
            return cls.query.filter_by(id=0), 0
        when = []
        for i in range(len(ids)):
            when.append((ids[i], i))
        return cls.query.filter(cls.id.in_(ids)).order_by(
            db.case(when, value=cls.id)), total

    @classmethod
    def before_commit(cls, session):
        session._changes = {
            'add': list(session.new),
            'update': list(session.dirty),
            'delete': list(session.deleted)
        }

    @classmethod
    def after_commit(cls, session):
        for obj in session._changes['add']:
            if isinstance(obj, SearchableMixin):
                add_to_index(obj.__tablename__, obj)
        for obj in session._changes['update']:
            if isinstance(obj, SearchableMixin):
                add_to_index(obj.__tablename__, obj)
        for obj in session._changes['delete']:
            if isinstance(obj, SearchableMixin):
                remove_from_index(obj.__tablename__, obj)
        session._changes = None

    @classmethod
    def reindex(cls):
        for obj in cls.query:
            add_to_index(cls.__tablename__, obj)

db.event.listen(db.session, 'before_commit', SearchableMixin.before_commit)
db.event.listen(db.session, 'after_commit', SearchableMixin.after_commit)




##Pulled from https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-viii-followers
followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    customername = db.Column(db.String(255), index=True)
    lastname = db.Column(db.String(255), index=True)
    middlename = db.Column(db.String(255))
    firstname = db.Column(db.String(255), index=True)
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
    reviews = db.relationship('Review', backref='user', lazy='dynamic')
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

    ##next 2 pulled from https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-x-email-support
    def get_reset_password_token(self, expires_in=600):
            return jwt.encode(
                {'reset_password': self.id, 'exp': time() + expires_in},
                current_app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, current_app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)

    def to_dict(self, include_email=False):
        data = {
            'id': self.id,
            'username': self.username,
            'lastname': self.lastname,
            'middlename': self.middlename,
            'firstname': self.firstname,
            'last_seen': self.last_seen.isoformat() + 'Z',
            'about_me': self.about_me,
            'address': self.address,
            'city': self.city,
            'country': self.country,
            'post_count': self.posts.count(),
            'follower_count': self.followers.count(),
            'followed_count': self.followed.count(),
            '_links': {
                'avatar': self.avatar(128)
            }
        }
        if include_email:
            data['email'] = self.email
        return data


class Post(SearchableMixin, db.Model):
    __searchable__ = ['body']

    body = db.Column(db.String(140))
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class Category(SearchableMixin, db.Model):
    __searchable__ = ['categoryname']

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
        return '<Employee {}>'.format(self.id)

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

    def to_dict(self):
        data = {
            'id': self.id,
            'order_id': self.order_id,
            'product_id': self.product_id,
            'order': self.order,
            'product': self.product,
            'quantity': self.quantity
        }
        return data


class Product(SearchableMixin, db.Model):
    __searchable__ = ['productname']
    id = db.Column(db.Integer, primary_key=True)
    productname = db.Column(db.String(255), index=True)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    unit = db.Column(db.Integer)
    price = db.Column(db.Numeric(scale=2, asdecimal=True))
    created = db.Column(db.DateTime, default=datetime.utcnow)
    orderdetails = db.relationship('OrderDetail', backref='product', lazy='dynamic')
    reviews = db.relationship('Review', backref='product', lazy='dynamic')


    def get_rating(self):
        ratings = []
        for rev in self.reviews:
            ratings.append(rev.rating)
            return sum(ratings)/float(len(ratings))



class Shipper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shippername = db.Column(db.String(255), index=True)
    phone = db.Column(db.String(25), index=True)
    orders = db.relationship('Order', backref='shipper', lazy='dynamic')


class Supplier(SearchableMixin, db.Model):
    __searchable__ = ['suppliername']
    id = db.Column(db.Integer, primary_key=True)
    suppliername = db.Column(db.String(255), index=True)
    contactname = db.Column(db.String(255), index=True)
    address = db.Column(db.String(255), index=True)
    city = db.Column(db.String(255), index=True)
    postalcode = db.Column(db.String(255), index=True)
    country = db.Column(db.String(255), index=True)
    phone = db.Column(db.String(25), index=True)
    products = db.relationship('Product', backref='supplier', lazy='dynamic')


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, index=True)
    review = db.Column(db.Text(1000))
    comments = db.Column(db.Text(300))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    product_id= db.Column(db.Integer, db.ForeignKey('product.id'))

    def top_rated(self):
        r = Review.query.group_by(Review.product_id).order_by(func.avg()).all()
        return r


@login.user_loader
def load_user(id):
    return User.query.get(int(id))