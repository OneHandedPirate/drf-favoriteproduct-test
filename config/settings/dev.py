from config.settings.base import *

DEBUG = True

MIDDLEWARE += [
    "silk.middleware.SilkyMiddleware",
]

INSTALLED_APPS += ["silk"]
