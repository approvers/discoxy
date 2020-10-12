import os
from urllib import parse


def get_env_or(environ_name, default):
    if environ_name not in os.environ.keys():
        return default
    return os.environ[environ_name]


def is_url(text):
    url_param = parse.urlparse(text)
    return len(url_param.scheme) > 0
