from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myproject.db'
db = SQLAlchemy(app)


class Rail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    direction = db.Column(db.String(20), nullable=False)
    times = db.Column(db.Integer, nullable=False)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/Schedule')
def schedule():
    return render_template('Schedule.html')


@app.route('/register_form')
def register_form():
    return render_template('register_form.html')


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)

