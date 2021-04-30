import os
from flask import render_template, request, session, Flask, g, redirect, flash, url_for, current_app
from functools import wraps
from database import DBManager
from model.user import User
from flask import Blueprint
from wtforms import Form, TextField, PasswordField, HiddenField, validators
from werkzeug.security import check_password_hash
import json

bp = Blueprint('login', __name__, url_prefix='/')

@bp.before_request
def get_db():
    '''Connects to the specific database.'''
    # 데이터베이스 처리
    DBManager.init('postgresql://mae:mae1234@localhost:5432/postgres', False) #DB매니저 클래스 초기화
    DBManager.init_db()
    print('get_db',g.db)

@bp.route('/user/login', methods=['POST'])
def login():

    form = LoginForm(request.form)
    next_url = form.next_url.data
    login_error = None
    
    if form.validate():
        session.permanent = True
    
        email= form.email.data
        password = form.password.data
        next_url = form.next_url.data
        
        print('(%s)next_url is %s' %(request.method, next_url))

        try:
            user = g.db.query(User).filter(User.email==email).first()
            print('-- ' + email + ' 비밀번호 -- : ' + user.password)
            print('-- 입력된 비밀번호 -- : ' + password)

        except Exception as e:
            print(str(e))
            raise e

        if user:
            print('check_password_hash : ', check_password_hash(user.password, password))
            if not check_password_hash(user.password, password):
                login_error = 'Invalid password'
                
            else:
                # 세션에 추가할 정보를 session 객체의 값으로 추가함
                # 가령, User 클래스 같은 사용자 정보를 추가하는 객체 생성하고
                # 사용자 정보를 구성하여 session 객체에 추가
                print('-- user -- : ', user.__dict__)
                # json_string = json.dumps(user)
                # print('-- json으로 변환됐나요? -- : ', json_string)

                # session['user_info'] = json.dumps(user.__dict__, separators=(',', ':'))
                session['user_info'] = user.email

                print('-- next_url -- : ', next_url)

                if next_url != '':
                    return redirect(next_url)
                else:
                    return redirect('/')
        else:
            login_error = 'User does not exist!'
            
    return render_template('layout.html', 
                   next_url=next_url, 
                   error=login_error, 
                   form=form)

@bp.route('/logout')
def logout():
    print('사용자 로그아웃')
    session.clear()
    return redirect('/')

def login_required(f):
    """현재 사용자가 로그인 상태인지 확인하는 데코레이터
    로그인 상태에서 접근 가능한 함수에 적용함
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):

        try:
            print(':::::: visited login_required')
            session_key = \
                request.cookies.get(
                    current_app.config['SESSION_COOKIE_NAME'])

            print(' -- session_key : ', session_key)
            print(' -- session.contains : ', session.__contains__('user_info'))

            is_login = False
            if session.__contains__('user_info'):
                is_login = True
            
            if not is_login:
                loginargs = 'login'
                next_url = request.form.get('next_url')
                print('next_url' , next_url)
                return redirect(url_for('product.main', islogin=loginargs))

            return f(*args, **kwargs)

        except Exception as e:
            print("Photolog error occurs : %s" %str(e))
            raise e

    return decorated_function

class LoginForm(Form):
    """로그인 화면에서 이메일과 비밀번호 입력값을 검증함"""
    email = \
            TextField('Email', 
                        [validators.Required('이메일을 입력하세요.'),
                        validators.Email(message='형식에 맞지 않는 이메일입니다.')])
        
    password = PasswordField('New Password', 
                [validators.Required('비밀번호를 입력하세요.'),
                 validators.Length(
                    min=4, 
                    max=50,
                    message='4자리 이상 50자리 이하로 입력하세요.')])
    
    next_url = HiddenField('Next URL')
