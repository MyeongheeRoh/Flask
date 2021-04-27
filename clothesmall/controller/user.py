import os
from flask import render_template, request, session, Flask, g, redirect, flash, jsonify
from database import DBManager
from model.user import User
from flask import Blueprint


bp = Blueprint('user', __name__, url_prefix='/')

@bp.before_request
def get_db():
    '''Connects to the specific database.'''
    # 데이터베이스 처리
    DBManager.init('postgresql://mae:mae1234@localhost:5432/postgres', False) #DB매니저 클래스 초기화
    DBManager.init_db()
    print('get_db',g.db)

@bp.route('/user/register')
def user():
    return render_template('register.html')

def __get_user(email):
    try:
        print('!!!!!!!!!!!!!!!!!!', email)
        current_user = g.db.query(User).filter(User.email == email).first()
        print('??????????????????', current_user)
        return current_user
    except Exception as e:
        print('__get_user_error', str(e))
        raise e

@bp.route('/user/check_email', methods=['POST'])
def check_email():
    print('--이메일 중복 체크--')
    email = request.get_json()
    print('이메일', email)
    #DB에서 email 중복확인
    if __get_user(email) == None :
        return jsonify(result = False)
    else:
        return jsonify(result = True)