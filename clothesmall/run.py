from create import create_app
from flask import render_template


app = create_app()

@app.route('/product/register')
def register_product_form():
    '''상품 등록을 위한 폼을 제공하는 함수'''
    print('상품 등록')
    return render_template('registerproduct.html')

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    print('Starting test server')
    app.run()
