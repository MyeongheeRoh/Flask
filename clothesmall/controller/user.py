import os
from flask import render_template, request, session, Flask, g, redirect, flash
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