

import os

from flask import Flask, render_template, current_app, session
from flask_talisman import Talisman
from auth.auth import oidc


def create_app():
    """
    Application Factory. A coomon pattern is creating the applciation
    object when the blueprint is imported. But if you move the creation
    of this object into a function, you can then create multiple instances
    of this app later.
    """
    csp = {
        'default-src': [
            '\'safe\'',
            '\'unsafe-inline\'',
            'stackpath.bootstrapcdn.com',
            'code.jquery.com',
            'cdn.jsdelivr.net',
            'cdnjs.cloudflare.com'
        ],
        'img-src': '\'self\' data:',
        'font-src': '*'
    }
    
    app = Flask(__name__)
    
    # if os.environ['FLASK_ENV'] == 'dev':
    #     app.config.from_pyfile('config/dev_app_config')
    # elif os.environ['FLASK_ENV'] == 'prod':
    #     app.config.from_file('config/app_config')
        
    # Talisman(app, content_security_policy=csp)
    # app.config['OIDC_CLIENT_SECRET'] = '/config/client_secrets.json'
    # app.config['OIDC_COOKIE_SECRET'] = True
    # # app.config['OIDC_CALLBACK_ROUTE'] = '/callback' # This is the default if you leave it as the default
    # # app.config['OVERWRITE_REDIRECT_URL'] = f'{app.config["BASE_URL"]}/callback' # Only needs to be enabled if redirect url is not the default
    # # app.config['OIDC_SCOPES'] = ['openid', 'email', 'profile', 'name'] # Be sure to check to see if this is what your provider needs 
    # app.secret_key = os.environ['SECRET_KEY']
    # oidc.init_app(app)
    
    @app.route("/", methods=['GET'])
    # @oidc.require_login
    def index():
        return render_template('index.html')


    @app.route("/about", methods=['GET'])
    # @oidc.require_login
    def about():
        return render_template('about.html')
    
    # with app.app_context():
        # Here is where you input your Blueprints
        # app.register_blueprint(<blueprint>)
    
    return app
    
    