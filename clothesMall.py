import psycopg2 as pg2
from flask import Flask, g, render_template, flash, request, session

app = Flask(__name__)

#TODO : 연결실패시 에러처리
#TODO : DB 정보 따로 빼거나 받을수 있도록
@app.before_request
def get_db():
    '''Connects to the specific database.'''
    conn_string = "host=localhost dbname=postgres user=mae password=mae1234 port=5432"
    if 'db' not in g:
        g.db = pg2.connect(conn_string)
        print('연결성공')

@app.teardown_appcontext
def close_connection(exception):
    db = g.pop('db', None)

    if db is not None:
        print('연결종료')
        db.close()

#TODO : 쿼리문 수행 실패시 에러처리?
def read_product_all():
    ret = tuple()
    cur = g.db.cursor()
    cur.execute('select * from product')
    ret = cur.fetchall()
    return ret

@app.route('/')
def shop_main():
    products = read_product_all()
    return render_template("product.html",data=products)

@app.route('/product/register', methods=['GET', 'POST'])
def register_product():
    '''Registers the product.'''
    
    #TODO : 관리자 로그인 했다고 가정, 로그인 이후 추가 필요
    error = None

    #유효성체크
    if request.method == 'POST':
        if not request.form['pname']:
            error = '상품명을 입력하세요.'
        elif not request.form['cost_price']:
            error = '원가를 입력하세요.'
        elif not request.form['selling_price']:
            error = '판매가를 입력하세요.'
        elif not request.form['product_info']:
            error = '상품정보를 입력하세요.'
        elif not request.form['category']:
            error = '카테고리를 입력하세요.' 
        else:

            try:
                cur = g.db.cursor()
                cur.execute('''INSERT INTO PRODUCT(ID, NAME, COST_PRICE, SELLING_PRICE, PRODUCT_INFORMATION, PRODUCT_CATEGORY) VALUES (NEXTVAL('PRODUCT_SEQ'), %s, %s, %s, %s, %s)''', [request.form['pname'], request.form['cost_price'], request.form['selling_price'], request.form['product_info'], request.form['product_category']])
                g.db.commit()
                flash('상품 등록이 완료되었습니다.')
            except Exception as e:
                g.db.rollback()
                flash('상품 등록이 실패했습니다.')
    
    return render_template("registerproduct.html", error=error)

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run()
