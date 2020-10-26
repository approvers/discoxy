import os
import platform
import configparser
from pathlib import Path
from typing import Optional
from tkinter.messagebox import *

from lib.model.utils import get_env_or
from lib.model.discord_entry import find_discord_entry_command

SECTION = 'discoxy'
CONFIG_PASS_DICT = {
    "Windows": get_env_or("APPDATA", "__INVALID_PLATFORM__") + "\\approvers\\discoxy\\config_cache.ini",
    "Darwin": get_env_or("HOME", "__INVALID_PLATFORM__") + "/.config/approvers/discoxy/config_cache.ini",
    "Linux": get_env_or("HOME", "__INVALID_PLATFORM__") + "/.config/approvers/discoxy/config_cache.ini"
}


class ConfigObject:
    def __init__(self):
        self.system = platform.system()

        self.config = configparser.ConfigParser()
        self.config_place = CONFIG_PASS_DICT[self.system]

        if os.path.isfile(self.config_place):
            try:
                self.config.read(self.config_place)
            except Exception as e:
                showerror(e)
                raise e
        else:
            # ファイルが存在しない場合、仮でからのプロパティをおいておく（これをしないとConfigParserの仕様で積みます）
            self.config.add_section(SECTION)
            self.config.set(SECTION, 'proxy_address', "")
            self.config.set(SECTION, 'port', "")

    def save_to_file(self) -> None:
        try:
            self.initialize_config_file()
            with open(self.config_place, 'w') as file:
                self.config.write(file)
        except Exception as e:
            showerror(f"設定ファイルの保存に失敗しました。既存の設定ファイルの削除をお試しください。: {e}")

    def initialize_config_file(self):
        if os.path.isfile(self.config_place):
            return

        dir_path = Path(self.config_place).parent
        os.makedirs(dir_path, exist_ok=True)

        try:
            with open(self.config_place, mode='w') as f:
                f.write("")
        except FileNotFoundError as e:
            showerror(f"設定ファイルの新規作成に失敗しました。\n内容: {e}")
        except Exception as e:
            showerror(f"不明なエラーが発生しました。\n内容: {e}")

    def set(self, proxy_address: str, port: int, discord_place: str = "") -> None:
        self.config.set(SECTION, 'proxy_address', proxy_address)
        self.config.set(SECTION, 'port', str(port))

        if discord_place == "":
            self.config.set(SECTION, 'discord_place',
                            find_discord_entry_command())
        else:
            self.config.set(SECTION, 'discord_place', discord_place)

    @property
    def proxy_address(self) -> str:
        return self.config.get(SECTION, "proxy_address")

    @property
    def port(self) -> Optional[int]:
        try:
            return int(self.config.get(SECTION, "port"))
        except ValueError:
            showerror("ポート番号の取得に失敗しました。設定ファイルの削除をお試しください。")
            return None

    @property
    def port_str(self) -> str:
        try:
            return str(self.config.get(SECTION, "port"))
        except ValueError:
            showerror("ポート番号の取得に失敗しました。設定ファイルの削除をお試しください。")
            return ""

    @property
    def discord_place(self) -> str:
        return self.config.get(SECTION, "discord_place")
