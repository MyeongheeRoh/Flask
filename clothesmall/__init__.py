import os
from flask import Flask


#애플리케이션 생성 함수
def create_app(mode='dev'):
    app = Flask(__name__)
    if mode == 'dev':
        app.config['DEBUG'] = True
    print('???')

    from .controller import product, user, login, category
    app.register_blueprint(product.bp)
    app.register_blueprint(user.bp)
    app.register_blueprint(login.bp)
    app.register_blueprint(category.bp)

    return app