import os
from flask import Flask
from .controller import *


#애플리케이션 생성 함수
def create_app(mode='dev'):
    app = Flask(__name__)
    if mode == 'dev':
        app.config['DEBUG'] = True
    print('???')

    from .clothesmall_blueprint import clothesmall
    app.register_blueprint(clothesmall)

    return app