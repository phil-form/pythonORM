from functools import wraps
from flask import redirect, session, url_for


def auth_required(level="USER", or_is_current_user=False):
    def auth_required_decorator(func):
        @wraps(func)
        def function_wrapper(*args, **kwargs):
            if session.get('userroles') and level in session.get('userroles'):
                return func(*args, **kwargs)

            if or_is_current_user and session.get('userid') and session.get('userid') == kwargs['userid']:
                return func(*args, **kwargs)

            return redirect(url_for('index'))

        return function_wrapper

    return auth_required_decorator
