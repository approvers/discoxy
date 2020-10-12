import os
from tkinter import *
from tkinter.ttk import *
from urllib import parse


def get_env_or(environ_name, default):
    if environ_name not in os.environ.keys():
        return default
    return os.environ[environ_name]


def space(frame: Frame, count: int):
    for _ in range(count):
        Label(frame, text="").pack()


def is_url(text):
    url_param = parse.urlparse(text)
    return len(url_param.scheme) > 0
