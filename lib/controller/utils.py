from urllib import parse


def is_url(text):
    url_param = parse.urlparse(text)
    return len(url_param.scheme) > 0
