import os
from flask import render_template, request, session, Flask, g, redirect, flash
from database import DBManager
from model.product import Product
from flask import Blueprint


bp = Blueprint('product', __name__, url_prefix='/')

@bp.before_request
def get_db():
    '''Connects to the specific database.'''
    # 데이터베이스 처리
    DBManager.init('postgresql://mae:mae1234@localhost:5432/postgres', False) #DB매니저 클래스 초기화
    DBManager.init_db()
    print('get_db',g.db)

def __get_product_all():
    '''상품목록 가져오기'''
    try:
        products = g.db.query(Product).order_by(Product.is_deleted, Product.id)
        return products 
     
    except Exception as e:
        print('error message',e)
        raise e

@bp.route('/')
def read_product_all():
    products = __get_product_all()
    return render_template('product.html', data = products)

def __create_product(name, cost_price, selling_price, admin_id, product_category, is_deleted):   
    try:
        product = Product(name, cost_price, selling_price, admin_id, product_category, is_deleted)
        g.db.add(product)
        g.db.commit()
        flash('상품 등록이 완료되었습니다.')
        
    except Exception as e:
        error = "DB error occurs : " + str(e)
        print(error)
        g.db.rollback()
        flash('상품 등록이 실패했습니다.')
        raise e


@bp.route('/product/register')
def register_product_form():
    '''상품 등록을 위한 폼을 제공하는 함수'''
    #TODO : 유효성체크 함수 만들기
    return render_template('editproduct.html')

@bp.route('/product/register', methods=['POST'])
def register_product():
    '''사용자 등록을 위한 함수'''

    try:
        name = request.form['pname']
        cost_price = request.form['cost_price']
        selling_price = request.form['selling_price']
        admin_id = 1
        product_category = request.form['category']
        is_deleted = 0

        if not name:
            error = '상품명이 없습니다.'
        elif not cost_price:
            error = '원가가 없습니다.'
        elif not selling_price:
            error = '판매가가 없습니다.'
        elif not product_category:
            error = '카테고리가 없습니다.'
        else:
            __create_product(name, cost_price, selling_price, admin_id, product_category, is_deleted)
        
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

@bp.route('/product/detail/<id>')
def read_product_detail(id):
    '''상품 상세 페이지'''
    print('************* 상품 아이디', id)
    product = __get_product_one(id)
    return render_template('productdetail.html', data = product)

@bp.route('/product/editform', methods=['POST'])
def modify_product_form():
    '''상품 수정을 위한 폼을 제공하는 함수'''
    #TODO : 유효성체크 함수 만들기
    id = request.form.get('product_id')
    product = __get_product_one(id)
    return render_template('editproduct.html', data = product)

def __modify_product_(id, name, cost_price, selling_price, product_category):
    try:
        g.db.query(Product).filter_by(id=id).update({'name':name, 'cost_price':cost_price, 'selling_price':selling_price, 'product_category':product_category})
        g.db.commit()
        print('상품 수정이 성공했습니다.')
     
    except Exception as e:
        error = "DB error occurs : " + str(e)
        print(error)
        g.db.rollback()
        print('상품 수정이 실패했습니다.')
        raise e


@bp.route('/product/edit', methods=['POST'])
def modify_product():
    '''상품목록 수정하기'''
    try:
        id = request.form['product_id']
        name = request.form['pname']
        cost_price = request.form['cost_price']
        selling_price = request.form['selling_price']
        product_category = request.form['category']

        if not id:
            error = '상품번호가 없습니다.'
        elif not name:
            error = '상품명이 없습니다.'
        elif not cost_price:
            error = '원가가 없습니다.'
        elif not selling_price:
            error = '판매가가 없습니다.'
        elif not product_category:
            error = '카테고리가 없습니다.'
        else:
            __modify_product_(id, name, cost_price, selling_price, product_category)

    except Exception as e:
        print('error message',e)
        raise e

    return redirect('/')

def __delete_product(id):
    try:
        product = g.db.query(Product).filter_by(id=id).first()
        print('delete::::::::::::', product)
        product.is_deleted = 1
        g.db.commit()
        print('상품 삭제가 성공했습니다.')
     
    except Exception as e:
        error = "DB error occurs : " + str(e)
        print(error)
        g.db.rollback()
        print('상품 삭제가 실패했습니다.')
        raise e

@bp.route('/product/delete', methods=['POST'])
def remove_product():
    id = request.form.get('product_id')
    print('remove_product:::::::::::', id)
    __delete_product(id)
    return redirect('/')