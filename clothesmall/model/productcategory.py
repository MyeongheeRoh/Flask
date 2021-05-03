from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import relationship
from ..model import Base


class ProductCategory(Base):
    __tablename__ = 'product_category'

    id_seq = Sequence('product_category_seq', metadata = Base.metadata)
    id = Column('id', Integer, id_seq, primary_key = True) 
    name = Column(String(45), unique = False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Product %r %r>' % (self.id, self.name)

