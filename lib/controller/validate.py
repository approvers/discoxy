from tkinter.messagebox import *
from typing import List

from lib.model.exceptions import InvalidParameterError
from lib.model.validator import validate_setting


def validation(law_inputs: List[str]) -> bool:
    proxy = law_inputs[0]
    port = law_inputs[1]
    place = law_inputs[2]

    try:
        validate_setting(proxy, port, place)
        return True
    except InvalidParameterError as e:
        showerror("", e)
        return False
