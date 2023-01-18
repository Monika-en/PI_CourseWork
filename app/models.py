from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from . import db, login_manager

class User(UserMixin, db.Model):
    # Create an User table
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    first_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    sign_up_date = db.Column(db.Date)
    activated  = db.Column(db.Integer, default=0)
    notifications = db.Column(db.Integer, default=1)
    type = db.Column(db.Integer, default=0)

    @property
    def password(self):
        # Prevent pasword from being accessed
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        # Set password to a hashed password
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        # Check if hashed password matches actual password
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Favourite(db.Model):
    __tablename__ = 'favourites'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    company_id = db.Column(db.Integer, nullable=False)

    # def __repr__(self):
        # return '<Favourites of {0}: {1}>'.format(self.type)

class Company(db.Model):
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    symbol = db.Column(db.String(12), nullable=False)
    industry = db.Column(db.String(64), nullable=False)
    stock_value = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(512), nullable=False)
    logo_url = db.Column(db.String(512), nullable=False)
    last_updated = db.Column(db.Date)
    def __repr__(self):
        return '<Company {0} ({1}), Price: {2}>'.format(self.name, self.symbol, self.stock_value)

class News(db.Model):
    __tablename__ = 'news'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(512), nullable=False)
    text = db.Column(db.String(4000), nullable=False)
    source_url = db.Column(db.String(1024), nullable=False)
    image_url = db.Column(db.String(1024), nullable=False)
    company_id = db.Column(db.Integer, nullable=False) 
    is_breaking = db.Column(db.Integer)
    date_time = db.Column(db.Date)
