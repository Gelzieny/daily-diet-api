import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from flask_login import UserMixin
from datetime import datetime
from database import db

class Refeicao(db.Model, UserMixin):
  __tablename__ = "refeicao"

  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(80), nullable=False, unique=True)
  description = db.Column(db.Text, nullable=True)
  date_time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
  is_within_diet = db.Column(db.Boolean, nullable=False)

  def __repr__(self):
    return f"<Refeicao {self.name}>"
