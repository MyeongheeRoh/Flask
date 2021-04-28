import os
from flask import render_template, request, session, Flask, g, redirect, flash, jsonify
from database import DBManager
from model.user import User
from flask import Blueprint
from wtforms import Form, TextField, PasswordField, HiddenField, validators
from werkzeug.security import generate_password_hash


bp = Blueprint('user', __name__, url_prefix='/')

@bp.before_request
def get_db():
    '''Connects to the specific database.'''
    # 데이터베이스 처리
    DBManager.init('postgresql://mae:mae1234@localhost:5432/postgres', False) #DB매니저 클래스 초기화
    DBManager.init_db()
    print('get_db',g.db)

'''사용자 등록 개발'''
@bp.route('/user/regist')
def user_registForm():
    form = RegisterForm(request.form)
    return render_template('register.html', form=form)

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

class RegisterForm(Form):
    """사용자 등록 화면에서 사용자명, 이메일, 비밀번호, 비밀번호 확인값을 검증함"""
    
    username = TextField('Username', 
                         [validators.Required('사용자명을 입력하세요.'),
                          validators.Length(
                            min=4, 
                            max=50, 
                            message='4자리 이상 50자리 이하로 입력하세요.')])
    
    email = TextField('Email', 
                      [validators.Required('이메일을 입력하세요.'),
                       validators.Email(message='형식에 맞지 않는 이메일입니다.')])
    
    password = \
        PasswordField('New Password', 
                      [validators.Required('비밀번호를 입력하세요.'),
                       validators.Length(
                        min=4, 
                        max=50,
                        message='4자리 이상 50자리 이하로 입력하세요.'),
                       validators.EqualTo('password_confirm', 
                                          message='비밀번호가 일치하지 않습니다.')])
        
    password_confirm  = PasswordField('Confirm Password')
    
    email_check = \
        HiddenField('Email Check', 
                    [validators.Required('이메일 중복을 확인하세요.')])