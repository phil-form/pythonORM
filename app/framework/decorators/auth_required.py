from functools import wraps
from flask import redirect, session, url_for

from app.framework.decorators.inject import inject
from app.services.auth_service import AuthService


def auth_required(level="USER", or_is_current_user=False):
    def auth_required_decorator(func):
        @wraps(func)
        @inject
        def function_wrapper(authService: AuthService, *args, **kwargs):
            current_user = authService.get_current_user()
            if level in current_user.get_roles():
                return func(*args, **kwargs)

            if or_is_current_user and current_user.userid == kwargs['userid']:
                return func(*args, **kwargs)

            return redirect(url_for('index'))

        return function_wrapper

    return auth_required_decorator
