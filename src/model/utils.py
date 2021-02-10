import os


def get_env_or(environ_name, default):
    if environ_name not in os.environ.keys():
        return default
    return os.environ[environ_name]
