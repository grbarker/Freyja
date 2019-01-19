##Form code initially taken from https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates
##then altered as necessary to fit the needs of the project
import collections
from sqlalchemy.sql import text
from sqlalchemy import create_engine, desc, func
from statistics import mean, median
from flask import render_template, flash, redirect, url_for, request, session
from sqlalchemy import asc, desc
from werkzeug.urls import url_parse
from datetime import datetime
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.models import User, Post, Employee, Product, Review
from app.email import send_password_reset_email
from app.forms import LoginForm, RegistrationForm, EmployeeRegistrationForm, \
    EditProfileForm, PostForm, ResetPasswordForm, ResetPasswordRequestForm, SortForm



@app.route('/product/<id>', methods=['GET', 'POST'])
def product(id):
    r = []
    product = Product.query.filter_by(id=id).first()
    for review in product.reviews:
        r.append(review.rating)
    rating = round(mean(r), 1)
    med = median(r)
    name = product.productname.capitalize()
    category = product.category
    #products is array of all the other products ordered by
    #the poeple who ordered the specified product
    products = []
    #The next array is the products bought together with the specified product
    #paired_products-->pp
    pps = []
    for od in product.orderdetails:
        orders = od.order.customer.orders.all()
        for o in orders:
            orderdetails = o.orderdetails.all()
            for od in orderdetails:
                product = od.product
                products.append(product)
    counted_products = collections.Counter(products).most_common(6)
    for od in product.orderdetails:
        order = od.order
        orderdetails = order.orderdetails.all()
        for od in orderdetails:
            p = od.product
            if p.id != product.id:
                pps.append(p)
    counted_pps = collections.Counter(pps).most_common(6)

    ##Not going to paginate the products as of now. The products are the top
    ##products also bought by people who ordered this product. The number has
    ##been limited to 8 so there is no need for pagination yet. It may be
    ##added later. Most likely there will just be a link to all the other
    ##products ordered by the people.Eventually the same functionality will
    ##be added for viewing a product.
    return render_template('product.html', title=name, product=product, name=name,
                           rating=rating, category=category, products=counted_products,
                           pps=counted_pps, median=med)


@app.route('/products', methods=['GET', 'POST'])
def products():
    form = SortForm()
    page = request.args.get('page', 1, type=int)
    sort = request.args.get('sort', 1, type=int)
    top_rated = False
    ##The sort arg of the request url is taken and compared to the hardcoded choices to find the
    ##matching choice, which is then taken from its place and put at
    ##the front of the array. This is done becase the SelectField of the form defaults to showing
    ##the first choice before the drop down is opened and it was desired to have the currently
    ##applied sort to be showing so it didn't confuse the user by showing Featured when the products
    ##are actually sorted by Price: Low to High. This will need to be addressed again when the choices
    ##array is decided upon(i.e. static or dynamic). So far I only needed a static, hardcoded set to work with.
    choices = [(1, 'Featured'), (2, 'Top Rated'), (3, 'Price: Low to High'), (4, 'Price: High to Low'), (5, 'Newest')]
    for choice in choices:
        if sort == choice[0]:
            choices.remove(choice)
            choices.insert(0, choice)
    ##The desired choice is put in the beginning of the choices array so it is shown as the default.
    form.sort_type.choices = choices
    if sort == 1:
        products = Product.query.paginate(page, 24, False)
    elif sort == 2:
        top_rated = True
        rs = Review.query.\
            with_entities(
                func.avg(Review.rating).label('average'),
                Review.product_id.label('product_id')).\
            group_by(Review.product_id).subquery()
        products = db.session.query(Product, rs).\
            join(rs, Product.id == rs.c.product_id).\
            order_by(desc(rs.c.average)).paginate(page, 24, False)
    elif sort == 3:
        products = Product.query.order_by(asc(Product.price)).paginate(page, 24, False)
    elif sort == 4:
        products = Product.query.order_by(desc(Product.price)).paginate(page, 24, False)
    elif sort == 5:
        products = Product.query.order_by(desc(Product.created)).paginate(page, 24, False)
    next_url = url_for('products', page=products.next_num, sort=sort) \
        if products.has_next else None
    prev_url = url_for('products', page=products.prev_num, sort=sort) \
        if products.has_prev else None
    if form.validate_on_submit():
        page = request.args.get('page', 1, type=int)
        #flash('Page: ' + str(page))
        #flash('Sort: ' + str(form.sort_type.data))
        sort = form.sort_type.data
        return redirect(url_for('products', sort=sort))
    return render_template('products.html', title='Products',
                           products=products.items, next_url=next_url,
                           prev_url=prev_url, form=form, top_rated=top_rated)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('index'))
    page = request.args.get('page', 1, type=int)
    posts = current_user.followed_posts().paginate(
        page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('index', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('index', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('index.html', title='Home', form=form,
                           posts=posts.items, next_url=next_url,
                           prev_url=prev_url)


@app.route('/explore')
@login_required
def explore():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('explore', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('explore', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template("index.html", title='Explore', posts=posts.items,
                          next_url=next_url, prev_url=prev_url)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


##Following function pulled from https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins.
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/register_employee', methods=['GET', 'POST'])
def register_employee():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = EmployeeRegistrationForm()
    if form.validate_on_submit():
        employee = Employee(employeeID=form.employee_id.data, lastname=form.lastname.data, firstname=form.firstname.data)
        employee.set_password(form.password.data)
        db.session.add(employee)
        db.session.commit()
        flash('Congratulations, you are now a registered employee!')
        return redirect(url_for('login'))
    return render_template('register_employee.html', title='Employee Register', form=form)


#from https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-x-email-support
@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('login'))
    return render_template('reset_password_request.html',
                           title='Reset Password', form=form)


##from https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-x-email-support
@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    posts = user.posts.order_by(Post.timestamp.desc()).paginate(
        page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('user', username=user.username, page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('user', username=user.username, page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('user.html', user=user, posts=posts.items,
                           next_url=next_url, prev_url=prev_url)


##Taken from https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vi-profile-page-and-avatars
@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)


##Next two pulled from https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-viii-followers
@app.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))
    if user == current_user:
        flash('You cannot follow yourself!')
        return redirect(url_for('user', username=username))
    current_user.follow(user)
    db.session.commit()
    flash('You are following {}!'.format(username))
    return redirect(url_for('user', username=username))


@app.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))
    if user == current_user:
        flash('You cannot unfollow yourself!')
        return redirect(url_for('user', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash('You are not following {}.'.format(username))
    return redirect(url_for('user', username=username))


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()