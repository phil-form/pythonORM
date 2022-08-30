from functools import wraps
from flask import redirect, session, url_for, request, jsonify

from app.framework.decorators.inject import inject
from app.services.auth_service import AuthService
from jwt import PyJWTError
import jwt
from app import app


def auth_required(level="USER", or_is_current_user=False):
    def auth_required_decorator(func):
        @wraps(func)
        @inject
        def function_wrapper(authService: AuthService, *args, **kwargs):
            token = None

            if 'x-access-tokens' in request.headers:
                token = request.headers['x-access-tokens']

            if 'Authorization' in request.headers:
                token = request.headers['Authorization']

            if not token:
                return redirect(url_for('index'))

            try:
                token = token.replace('Bearer ', '')
                current_user = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
                print(current_user)
                print(type(current_user))
            except PyJWTError as e:
                print(e)
                return redirect(url_for('index'))

            authService.set_current_user(current_user)
            if level in current_user['roles']:
                return func(*args, **kwargs)

            if or_is_current_user and current_user['userid'] == kwargs['userid']:
                return func(*args, **kwargs)

            return redirect(url_for('index'))

        return function_wrapper

    return auth_required_decorator
