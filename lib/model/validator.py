import os

from compose.config import is_url

from lib.model.exceptions import InvalidParameterError


def validate_setting(address: str, port: str, discord_path: str):
    valid_url = is_url(address)
    valid_port = port.isnumeric() and (0 <= int(port) <= 65535)
    valid_path = os.path.isfile(discord_path)

    if not(valid_url and valid_port and valid_path):
        raise InvalidParameterError(not valid_url, not valid_port, not valid_path)
