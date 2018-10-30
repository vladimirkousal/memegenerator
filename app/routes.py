from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, EditProfileForm
from flask_login import current_user, login_user
from app.models import User
from app.forms import RegistrationForm
from flask_login import logout_user, login_required
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    posts = [
        {
            
        },
        {
            
        }
    ]
    return render_template('index.html', title='Test')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Neplatné jméno či heslo.')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Test', form=form)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for("index"))

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
        flash('Byl jsi registrován(a)')
        return redirect(url_for('login'))
    return render_template('register.html', title='Registrace', form=form)

@app.route("/<username>")
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}

    ]
    return render_template('user.html', user=user, posts=posts, title="Profil")

@app.before_request
def before_request():
	if current_user.is_authenticated:
		current_user.last_seen = datetime.utcnow()
		db.session.commit()

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Změny byly uloženy.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Upravit Profil', form=form)

@app.route("/random_meme")
def random_meme():
    return render_template("random_meme.html", title="Random meme")

@app.route("/rozvrh")
def rozvrh():
    return render_template("rozvrh.html", title="Rozvrh V1C")

@app.route("/countdown")
def countdown():
    return render_template("padkocountdown.html", title="PaDko countdown")

@app.route("/disclaimer")
def disclaimer():
    return render_template("disclaimer.html", title="Disclaimer")