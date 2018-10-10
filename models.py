from datetime import datetime
from app import db, bcrypt
from enums import UserRoles


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(2550), unique=False, nullable=False)
    first_name = db.Column(db.String(100), unique=False, nullable=True)
    last_name = db.Column(db.String(100), unique=False, nullable=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    user_role = db.Column(db.Integer, db.ForeignKey('user_role_id'))

    def __init__(self, id, username, first_name, last_name, email, user_role, password):
        self.id = id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.user_role = user_role
        self.password = bcrypt.generate_password_hash(password)


class UserRole(db.Model):
    __tablename__ = "user_roles"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    role = db.Column(db.Enum(UserRoles), unique=False, nullable=False)
    users = db.relationship('User', backref='user_roles', lazy=True)

    def __init__(self, role):
        self.role = role