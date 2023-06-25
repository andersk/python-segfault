from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.urls import path
from django.views.decorators.csrf import csrf_protect


def wrap(func):
    return lambda *args, **kwargs: func(*args, **kwargs)


def bar():
    try:
        raise ValidationError("")
    except ValidationError:
        raise Exception


@wrap
@wrap
def foo(request, user):
    user.username
    try:
        bar()
    except Exception:
        return HttpResponse()


@wrap
@wrap
@wrap
@wrap
@csrf_protect
def me(request):
    return foo(request, request.user)


urlpatterns = [path("me", me)]
