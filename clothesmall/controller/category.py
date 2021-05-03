from flask import Blueprint
from flask import render_template, g
from ..database import DBManager
from ..model.productcategory import ProductCategory


bp = Blueprint('category', __name__, url_prefix='/')

@bp.before_request
def get_db():
    '''Connects to the specific database.'''
    # 데이터베이스 처리
    DBManager.init('postgresql://mae:mae1234@localhost:5432/postgres', False) #DB매니저 클래스 초기화
    DBManager.init_db()
    print('get_db',g.db)

def __get_category_all():
    '''상품 카테고리 가져오기'''
    try:
        categories = g.db.query(ProductCategory).order_by(ProductCategory.id)
        return categories
     
    except Exception as e:
        print('error message',e)
        raise e

@bp.route('/category/list')
def read_category_all():
    print('*'*100)
    print('/category/list')
    print('*'*100)
    category = __get_category_all()
    return render_template('category.html', categories = category)