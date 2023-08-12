
import functools
from lib2to3.pgen2 import token
import os

import google.auth.transport.requests
import requests
from flask import Blueprint, abort
from flask import current_app as app
from flask import redirect, request, session, url_for
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
from flask_oidc import OpenIDConnect

# Used For OIDC Okta
oidc = OpenIDConnect()

### Uncomment For Google OAuth
# auth_bp = Blueprint(
#     'auth_bp', __name__, static_folder='static', template_folder='templates'
# )

# def get_client():
#     """Instantiastes OAuth2 Client"""
    
#     if os.environ['FLASK_ENV'] == 'development':
#         client_secrets_file = '/client/service-catalog-client-secrets-dev'
#     elif os.environ['FLASK_ENV'] == 'production':
#         client_secrets_file = '/client/service-catalog-client-secret'
    
#     flow = Flow.from_client_secrets_file(
#         client_secrets_file=client_secrets_file,
#         scopes=[
#             "https://www.googleapis.com/auth/userinfo.profile",
#             "https://www.googleapis.com/auth/userinfo.email",
#             "openid"
#         ],
#         redirect_uri=f'{app.config["BASE_URL"]}/callback'
#     )
#     return flow

# def login_is_required(function):
#     """Decorator for all application endpoints that ensures a user is logged in"""
    
#     @functools.wraps(function)
#     def wrapper(*args, **kwargs):
#         if 'google_id' not in session:
#             session['referrer'] = request.url
#             return redirect(url_for('auth_bp.login'))
#         return function(**args, **kwargs)
    
#     return wrapper

# @auth_bp.route('/login')
# def login():
#     """Responsible for OAuth2 authentication"""
    
#     flow = get_client()
#     authorization_url, state = flow.authorization_url()
#     session['state'] = state
#     return redirect(authorization_url)


# @auth_bp.route('/callback')
# def callback():
#     """Callback stores returned metadata and keys following authentication"""
    
#     flow = get_client()
#     flow.fetch_token(authorization_response=request.url)
    
#     if not session['state'] == request.args['state']:
#         abort(500) # State does not match
        
#     credentails = flow.credentials
#     request_session = requests.session()
#     cached_session = cachecontrol.CacheControl(request_session)
#     token_request = google.auth.transport.requests.Request(session=cached_session)
    
#     id_info = id_token.verify_oauth2_token(
#         id_token=credentails._id_token,
#         request=token_request,
#         audience=app.config['GOOGLE_CLIENT_ID']
#     )
    
#     session['raw'] = id_info
#     session['google_id'] = id_info.get('sub')
#     session['name'] = id_info.get('name')
#     session['email'] = id_info.get('email')
#     return redirect(session['referrer'])

# @auth_bp.route('/logout')
# @login_is_required
# def logout():
#     """Logs the user out of their session"""
    
#     session.clear()
#     return redirect('/')