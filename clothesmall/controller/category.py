from flask import render_template, g

from ..database import DBManager
from ..model.productcategory import ProductCategory
from ..clothesmall_blueprint import clothesmall


def __get_category_all():
    '''상품 카테고리 가져오기'''
    try:
        categories = g.db.query(ProductCategory).order_by(ProductCategory.id)
        print(categories)
        return categories
     
    except Exception as e:
        print('error message',e)
        raise e

@clothesmall.route('/category/list')
def read_category_all():
    '''상품의 카테고리 목록 전체를 보여준다.'''
    print('*'*100)
    print('/category/list')
    print('*'*100)
    category = __get_category_all()
    return render_template('category.html', categories = category)