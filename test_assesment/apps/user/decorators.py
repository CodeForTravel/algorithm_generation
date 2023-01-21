
from functools import wraps
from django.http import HttpResponseForbidden
from test_assesment.apps.user.models import User

def is_admin(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user and request.user.user_type != User.UserTypes.ADMIN:
            return HttpResponseForbidden()
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def is_staff_user(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user and request.user.user_type != User.UserTypes.STAFF:
            return HttpResponseForbidden()
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def is_general(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user and request.user.user_type != User.UserTypes.GENERAL:
            return HttpResponseForbidden()
        return view_func(request, *args, **kwargs)
    return _wrapped_view