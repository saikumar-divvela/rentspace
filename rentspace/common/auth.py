import re

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


class LoginMiddleware(object):
    def __init__(self):
        self.staff_required = tuple(re.compile(url) for url in settings.STAFF_REQUIRED_URLS)
        self.login_required = tuple(re.compile(url) for url in settings.LOGIN_REQUIRED_URLS)
        self.exceptions = tuple(re.compile(url) for url in settings.LOGIN_REQUIRED_URLS_EXCEPTIONS)

    def process_view(self, request, view_func, view_args, view_kwargs):
        print (" Common auth is called *****************************")

        for url in self.exceptions:
            if url.match(request.path):
                return None


        # For admin required url check if user is logged in and staff otherwise redirect to login_required
        for url in self.staff_required:
            if url.match(request.path):
                if request.user.is_authenticated and request.user.is_staff:
                    return None
                else:
                    return user_passes_test(lambda u: u.is_staff)(view_func)(request, * view_args, **view_kwargs)

        if request.user.is_authenticated():
            return None

        for url in self.login_required:
            if url.match(request.path):
                return login_required(view_func)(request, * view_args, **view_kwargs)

        # Explicitly return None for all non - matching requests
        return None