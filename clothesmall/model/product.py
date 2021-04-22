from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import relationship
from model import Base


class Product(Base):
    __tablename__ = 'product'

    id_seq = Sequence('product_seq', metadata = Base.metadata)
    id = Column('id', Integer, id_seq, primary_key = True) 
    name = Column(String(45), unique = False)
    cost_price = Column(Integer, unique = False)
    selling_price = Column(Integer, unique = False)
    admin_id = Column(Integer, unique = False)
    product_category = Column(Integer, unique = False)

    def __init__(self, name, cost_price, selling_price, admin_id, product_category):
        self.name = name
        self.cost_price = cost_price
        self.selling_price = selling_price
        self.admin_id = admin_id
        self.product_category = product_category
    
    def __repr__(self):
        return '<Product %r %r %r %r %r %r>' % (self.id, self.name, self.cost_price, self.selling_price, self.admin_id, self.product_category)

