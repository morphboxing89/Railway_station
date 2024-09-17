from app import db
from flask_login import UserMixin


class Train(db.Model):
    __tablename__ = 'train'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    direction = db.Column(db.String(20), nullable=False)
    times = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'Направление: {self.direction} Номер поезда: {self.number} Время отправления: {self.times}'


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return f'<User: {self.username}>'

    def get_id(self):
        return self.uid
