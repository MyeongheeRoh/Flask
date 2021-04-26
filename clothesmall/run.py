from create import create_app
from flask_bootstrap import Bootstrap

app = create_app()
Bootstrap(app)

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    print('Starting test server')
    app.run()