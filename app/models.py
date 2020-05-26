from flask_sqlalchemy import SQLAlchemy
from app.config import *
from datetime import datetime
from app.data import *



db = SQLAlchemy(app)


class Hospital(db.Model):
    __tablename__ = 'region'
    id = db.Column(db.String(36), primary_key=True)
    hospital_name = db.Column(db.String(64), nullable=False)
    hospital_code = db.Column(db.String(5), nullable=False)
    hospital_city = db.Column(db.String(64), nullable=False)
    hospital_country = db.Column(db.String(64), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<{self.id}:{self.hospital_name}"


db.create_all()