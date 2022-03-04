from app.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
import re
import bcrypt

salt = bcrypt.gensalt()

class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String(50), nullable=False)
  email = Column(String(50), nullable=False, unique=True)
  password = Column(String(100), nullable=False)

  @validates('email')
  def email_validator(self, key, email):
    assert re.match(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', email) != None
    return email

  @validates('password')
  def password_validator(self, key, password):
    assert len(password) > 8
    return bcrypt.hashpw(password.encode('utf-8'), salt)

  def verify_password(self, password):
    return bcrypt.checkpw(
      password.encode('utf-8'),
      self.password.encode('utf-8')
    )