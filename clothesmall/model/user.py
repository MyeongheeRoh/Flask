from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import relationship
from marshmallow import Schema, fields
from ..model import Base


class User(Base):
    __tablename__ = 'user'

    id_seq = Sequence('user_seq', metadata = Base.metadata)
    id = Column('id', Integer, id_seq, primary_key = True) 
    password = Column(String(45), unique = False)
    name = Column(String(45), unique = False)
    phone_number = Column(String(20), unique = False)
    status = Column(String(10), unique = False)
    email = Column(String(45), unique = True)
    role = Column(String(10), unique = False)
    is_deleted = Column(Integer, unique = False)

    def __init__(self, password, name, phone_number, status, email, role, is_deleted):
        self.password = password
        self.name = name
        self.phone_number = phone_number
        self.status = status
        self.email = email
        self.role = role
        self.is_deleted = is_deleted

    def __repr__(self):
        return '<Product %r %r %r %r %r %r %r %r>' % (self.id, self.password, self.name, self.phone_number, self.status, self.email, self.role, self.is_deleted)

class UserSchema(Schema):
    id = fields.Int()
    password = fields.Str()
    name = fields.Str()
    phone_number = fields.Str()
    status = fields.Str()
    email = fields.Str()
    role = fields.Str()
    is_deleted = fields.Int()
