import os
from typing import Optional, List

from lib import utils
from lib.controller import ProxySetting


def parse(law_inputs: List[str]) -> Optional[ProxySetting]:
    proxy = law_inputs[0]
    port = law_inputs[1]
    place = law_inputs[2]

    if not validation(proxy, port, place):
        return

    ret = ProxySetting(proxy_address=proxy, port=port)
    return ret


def validation(proxy: str, port: str, place: str) -> bool:
    # URLチェック
    if not utils.is_url(proxy):
        utils.error_dialog("アドレスが無効です。正しいURLを入力してください。")
        return False

    # ポート番号チェック
    try:
        if not (0 <= int(port) <= 65535):
            raise RuntimeError("Invalid port number has passed. Please specify port number in range of 0 ~ 65535.")
    except Exception as e:
        utils.error_dialog(e)
        return False

    # ファイルチェック
    if not os.path.exists(place):
        utils.error_dialog("ファイルが見つかりませんでした。パスを確認してください。")
        return False

    return True
