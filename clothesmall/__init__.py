import os
from flask import Flask
from .controller import *
from .database import DBManager

app = Flask(__name__)

#애플리케이션 생성 함수
def create_app():

    print('*'*100)
    print('create app')
    print('*'*100)

    # 기본 설정은 PhotologConfig 객체에 정의되있고 운영 환경 또는 기본 설정을 변경을 하려면
    # 실행 환경변수인 PHOTOLOG_SETTINGS에 변경할 설정을 담고 있는 파일 경로를 설정 
    from .config import ClothesmallConfig
    app.config.from_object(ClothesmallConfig)
    #기본 클래스와 설정 변경하기 위해 적용할 설정파일 설정

    from .clothesmall_blueprint import clothesmall
    app.register_blueprint(clothesmall)

    with app.app_context():
        before_request()
    
    return app

@app.before_request
def before_request():
    db_url = app.config['DB_URL']
    DBManager.init(db_url, eval(app.config['DB_LOG_FLAG'])) #DB매니저 클래스 초기화
    DBManager.init_db()