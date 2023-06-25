AUTHENTICATION_BACKENDS = ["myapp.auth.MyAuthBackend"]
AUTH_USER_MODEL = "myapp.MyUser"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite3",
    }
}
DEBUG = True
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "myapp",
]
MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    *(["django.utils.deprecation.MiddlewareMixin"] * 15),
]
ROOT_URLCONF = "myapp.urls"
SECRET_KEY = "sekrit"
