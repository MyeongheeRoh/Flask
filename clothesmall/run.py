from create import create_app
from flask import render_template, request, session, g, redirect, flash
from database import DBManager
from model.product import Product


app = create_app()

@app.before_request
def get_db():
    '''Connects to the specific database.'''
    # 데이터베이스 처리
    DBManager.init('postgresql://mae:mae1234@localhost:5432/postgres', False) #DB매니저 클래스 초기화
    DBManager.init_db()
    print('get_db',g.db)

def __get_product_all():
    '''상품목록 가져오기'''
    try:
        products = g.db.query(Product)
        return products 
     
    except Exception as e:
        print('error message',e)
        raise e

@app.route('/')
def read_product_all():
    products = __get_product_all()
    return render_template('product.html', data = products)

@app.route('/product/register')
def register_product_form():
    '''상품 등록을 위한 폼을 제공하는 함수'''
    #TODO : 유효성체크 함수 만들기
    return render_template('editproduct.html')

@app.route('/product/register', methods=['POST'])
def register_product():
    '''사용자 등록을 위한 함수'''

    if not request.form['pname']:
        error = '상품명을 입력하세요.'
    elif not request.form['cost_price']:
        error = '원가를 입력하세요.'
    elif not request.form['selling_price']:
        error = '판매가를 입력하세요.'
    elif not request.form['category']:
        error = '카테고리를 입력하세요.'
    else:

        try:
            name = request.form['pname']
            cost_price = request.form['cost_price']
            selling_price = request.form['selling_price']
            admin_id = 1
            product_category = request.form['category']
            
            product = Product(name, cost_price, selling_price, admin_id, product_category)
            g.db.add(product)
            g.db.commit()
            flash('상품 등록이 완료되었습니다.')
        
        except Exception as e:
            error = "DB error occurs : " + str(e)
            print(error)
            g.db.rollback()
            flash('상품 등록이 실패했습니다.')
            raise e

    return redirect('/')
    
def __get_product_one(id):
    try:
        product = g.db.query(Product).filter_by(id=id).one()
        return product 
     
    except Exception as e:
        print(str(e))
        raise e

@app.route('/product/detail/<id>')
def read_product_detail(id):
    '''상품 상세 페이지'''
    print('*************', id)
    product = __get_product_one(id)
    return render_template('productdetail.html', data = product)

@app.route('/product/edit', methods=['POST'])
def modify_product():
    '''상품목록 수정하기'''
    try:
        products = g.db.query(Product).filter(id == 1).update({'cost_price':6000})
        g.db.commit()

    except Exception as e:
        print('error message',e)
        raise e

    else:
        return redirect('/')


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    print('Starting test server')
    app.run()
