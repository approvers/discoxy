from tkinter.messagebox import *
from typing import List, Optional

from lib.model.config_object import ConfigObject

from lib.model.exceptions import InvalidParameterError
from lib.model.validator import validate_setting


def parse(law_inputs: List[str]) -> Optional[ConfigObject]:
    proxy = law_inputs[0]
    port = law_inputs[1]
    place = law_inputs[2]

    if not validation(proxy, port, place):
        return

    ret = ConfigObject(proxy_address=proxy, port=(port), discord_place=place)
    return ret


def validation(proxy: str, port: str, place: str) -> bool:
    try:
        validate_setting(proxy, port, place)
        return True
    except InvalidParameterError as e:
        showerror("", e)
        return False
