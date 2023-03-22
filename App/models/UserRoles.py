from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from flask import jsonify
from flask_login import UserMixin
from datetime import datetime

class UserRoles(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('role.id', ondelete='CASCADE'))

    

