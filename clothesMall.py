import psycopg2 as pg2
from flask import Flask, g, render_template

app = Flask(__name__)

@app.before_request
def get_db():
    """Connects to the specific database."""
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

def read_product_all():
    ret = list()
    cur = g.db.cursor()
    cur.execute('select * from product')
    ret = cur.fetchall()
    return ret

@app.route('/')
def shop_main():
    products = read_product_all()
    return render_template("layout.html",data=products)

if __name__ == '__main__':
    app.run()
