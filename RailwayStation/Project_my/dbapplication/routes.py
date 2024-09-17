from flask import render_template, request, redirect, url_for, flash
from flask_login import logout_user, login_user

from models import Train
from models import User


def register_routes(app, db, bcrypt):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/Schedule')
    def schedule():
        train = Train.query.all()
        return render_template('Schedule.html', train=train)

    @app.route('/register_form', methods=['GET', 'POST'])
    def register_form():
        if request.method == 'GET':
            return render_template('register_form.html')
        elif request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            email = request.form.get('email')

            hashed_password = bcrypt.generate_password_hash(password)

            user = User(username=username, password=hashed_password, email=email)

            db.session.add(user)
            db.session.commit()
            flash(f'Поздравляем, {username}! Вы зарегестрировались', 'success')
            return redirect(url_for('login'))

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            user = User.query.filter_by(username=request.form.get('username')).first()
            password = request.form.get('password')
            if user and bcrypt.check_password_hash(user.password, password):
                login_user(user)
                return render_template('index.html')
            else:
                flash('Ошибка входа. Проверьте имя и пароль', 'danger')
        return render_template('login.html')

    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('index'))
