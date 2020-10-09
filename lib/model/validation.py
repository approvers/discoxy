import os
import time
from typing import List

from lib.model import utils


def validation(law_inputs: List[str]) -> None:
    proxy = law_inputs[0]
    port = law_inputs[1]
    place = law_inputs[2]

    print(time.time())

    if not utils.is_url(proxy):
        utils.error_dialog("Invalid address has passed. Please specify valid URL.")
        return

    try:
        port = int(port)
    except Exception as e:
        utils.error_dialog(e)
        return

    if not (0 <= port <= 65535):
        utils.error_dialog("Invalid port number has passed. Please specify within 0 ~ 65535.")
        return

    try:
        if not os.path.exists(place):
            raise FileNotFoundError("File not found. Please check your file.")
    except Exception as e:
        utils.error_dialog(e)
        return
