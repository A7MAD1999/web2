from VAG.models import User , Feature , Project
from flask import render_template ,redirect,url_for ,flash , request
from VAG.forms import RegistrationForm , LoginForm 
from VAG import app , bcrypt, db
from flask_login import login_user , current_user , logout_user ,login_required


features = [
    {
        "title": "Request",
        "course": "",
        "author": "",
        "thumbnail": "B2.jpg",
    },
    {
        "title": "Request",
        "course": "",
        "author": "",
        "thumbnail": "B2.jpg",
    },
    {
        "title": "Request",
        "course": "",
        "author": "",
        "thumbnail": "B2.jpg",
    },
    {
        "title": "Request",
        "course": "",
        "author": "",
        "thumbnail": "B2.jpg",
    },
#     {
#         "title": "Request",
#         "course": "",
#         "author": "",
#         "thumbnail": "B2.jpg",
#     },
#     {
#         "title": "Request",
#         "course": "",
#         "author": "",
#         "thumbnail": "B2.jpg",
#     },
]
projects = [
    {
        "name": "Python",
        "icon": "B2.jpg",
        "description": "",
    },
    {
        "name": "Data Analysis",
        "icon": "B2.jpg",
        "description": "",
    },
    {
        "name": "Machine Learning",
        "icon": "B2.jpg",
        "description": "",
    },
    {
        "name": "Web Design",
        "icon": "B2.jpg",
        "description": "",
    },
    {
        "name": "Blockchain",
        "icon": "B2.jpg",
        "description": "",
    },
    {
        "name": "Tips & Tricks",
        "icon": "B2.jpg",
        "description": "",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', features=features,projects=projects)

@app.route("/about")
def about():
    return render_template('about.html', title="About")

@app.route("/register",methods=["GET","POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(fname = form.fname.data , lname = form.lname.data , username = form.username.data , email = form.email.data , password = hashed_password )
        db.session.add(user)
        db.session.commit()
        flash(f"Account created!, Hi {form.username.data}", 'success') 
        return redirect(url_for("login"))
    return render_template('register.html' , title='Register' , form=form)

@app.route("/login",methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remember.data)
            next_page = request.args.get('next')
            flash('You have been logged in!','success')
            return redirect(next_page) if next_page else (url_for("home"))
        else:
            flash('login Unsuccessful. Please check credentials', 'danger')
    return render_template('login.html', title='Login',form=form)

@app.route("/contact")
def contact():
    return render_template('contact.html', title="Contact")

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template('dashboard.html', title="Dashboard")


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))