import os
from flask import render_template, request, session, Flask, g, redirect, flash, jsonify, url_for
from wtforms import Form, TextField, PasswordField, HiddenField, validators
from werkzeug.security import generate_password_hash

from ..database import DBManager
from ..model.user import User
from ..clothesmall_blueprint import clothesmall


@clothesmall.route('/user/unregist')
def unregist():
    '''사용자 삭제'''
    print('*'*100)
    print(session['user_info'].email)
    print('*'*100)
    email = session['user_info'].email
    print('-- 삭제 요청 이메일 : ', email)

    try:
        #사용자의 is_deleted 상태를 1로 바꾸어 삭제로 변경
        current_user = __get_user(email)
        current_user.is_deleted = 1
        g.db.commit()
        print('사용자 삭제 처리')
    
    except Exception as e:
        print('사용자 삭제에 실패했습니다.' + str(e))
        g.db.rollback()
        raise e

    else:
        # 성공적으로 사용자 탈퇴가 되면, 로그아웃
        return redirect(url_for('login.logout'))


@clothesmall.route('/user/<email>')
def update_user_form(email):
    '''사용자 수정 폼으로 이동 '''
    print('-- 사용자 수정 폼 --', email)
    current_user = __get_user(email)
    form = UpdateForm(request.form, current_user)

    return render_template('register.html',
                            user=current_user,
                            form=form)

@clothesmall.route('/user/<email>', methods=['POST'])
def update_user(email):
    '''사용자 수정'''
    current_user = __get_user(email)
    form = UpdateForm(request.form)

    if form.validate():
        name = form.name.data
        password = form.password.data
                  
        try:
            current_user.name = name
            current_user.password = generate_password_hash(password)
            g.db.commit()
            print('-- 사용자 수정 성공! --')

        except Exception as e:
            g.db.rollback()
            print(str(e))
            raise e
        else:
            data = 'success'
            # 성공적으로 사용자 등록이 되면, 로그인 화면으로 이동.
            return render_template('layout.html', isregist=data)
    else:
        return render_template('register.html', 
                               user=current_user, 
                               form=form)

def __get_user(email):
    '''email이 일치하는 사용자 한명의 객체를 가져온다.'''
    try:
        current_user = g.db.query(User).filter(User.email == email).first()

        print(current_user.__dict__)
        return current_user 
     
    except Exception as e:
        print(str(e))
        raise e

@clothesmall.route('/user/regist')
def user_registForm():
    '''사용자 등록 폼'''
    form = RegisterForm(request.form)
    return render_template('register.html', form=form)

@clothesmall.route('/user/regist', methods=['POST'])
def register_user():
    '''사용자 등록'''
    print('-- retister_user start')
    form = RegisterForm(request.form)

    print('-- form-validate() ', form.validate())

    if form.validate():

        password = form.password.data
        name = form.name.data
        phone_number = form.phone_number.data
        status = ''
        email = form.email.data
        role = 'USER'
        is_deleted = 0

        print('-- 넘어온 회원 값 : ' + password + ' ' + name + ' ' + email)

        try:            
            user = User(generate_password_hash(password), name, phone_number, status, email, role, is_deleted)
            g.db.add(user)
            g.db.commit()
            print('-- regist_user : ', user) 
            
        except Exception as e:
            error = "DB error occurs : " + str(e)
            print(error)
            g.db.rollback()
            raise e
        
        else:
            print('-- 회원 가입 성공 --')
            data = 'success'
            # 성공적으로 사용자 등록이 되면, 로그인 화면으로 이동.
            return render_template('layout.html', isregist=data)
    else:
        return render_template('register.html', form=form)

@clothesmall.route('/user/check_email', methods=['POST'])
def check_email():
    '''이메일 중복 체크'''
    
    email = request.json['email']
    print('이메일', email)
    #DB에서 email 중복확인
    if __get_user(email) == None :
        return jsonify(result = False)
    else:
        return jsonify(result = True)

class UpdateForm(Form):
    """사용자 등록 화면에서 사용자명, 핸드폰번호, 이메일, 비밀번호, 비밀번호 확인값을 검증함"""
    
    email = TextField('Email')
 
    name = TextField('Username', 
                         [validators.Required('사용자명을 입력하세요.'),
                          validators.Length(
                            min=4, 
                            max=50, 
                            message='4자리 이상 50자리 이하로 입력하세요.')])
    
    phone_number = TextField('phonenumber', 
                         [validators.Required('형식에 맞게 전화번호를 입력해주세요. (ex : 01012345678)'),
                          validators.Length(
                            min=9, 
                            max=11, 
                            message='9자리 이상 11자리 이하로 입력하세요.')])
    
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

class RegisterForm(Form):
    """사용자 등록 화면에서 사용자명, 이메일, 비밀번호, 비밀번호 확인값을 검증함"""
    
    email = TextField('Email', 
                      [validators.Required('이메일을 입력하세요.'),
                       validators.Email(message='형식에 맞지 않는 이메일입니다.')])
 
    name = TextField('Username', 
                         [validators.Required('사용자명을 입력하세요.'),
                          validators.Length(
                            min=4, 
                            max=50, 
                            message='4자리 이상 50자리 이하로 입력하세요.')])
    
    phone_number = TextField('phonenumber', 
                         [validators.Required('형식에 맞게 전화번호를 입력해주세요. (ex : 01012345678)'),
                          validators.Length(
                            min=9, 
                            max=11, 
                            message='9자리 이상 11자리 이하로 입력하세요.')])
    
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