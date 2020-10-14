import configparser
import platform

from lib.model.discord_entry import find_discord_entry_command
from lib.model.utils import get_env_or
from lib.model.validator import validate_setting

SECTION = 'discoxy'
CONFIG_PASS_DICT = {
    "Windows": get_env_or("APPDATA", "__INVALID_PLATFORM__") + "\\approvers\\discoxy\\config_cache.ini",
    "Darwin": get_env_or("HOME", "__INVALID_PLATFORM__") + "/.config/approvers/discoxy/config_cache.ini",
    "Linux": get_env_or("HOME", "__INVALID_PLATFORM__") + "/.config/approvers/discoxy/config_cache.ini"
}


class ConfigObject:
    def __init__(self, proxy_address: str, port: int, discord_place: str = ""):
        self.system = platform.system()

        self.config = configparser.ConfigParser()
        self.config_place = CONFIG_PASS_DICT[self.system]

        self.config.add_section(SECTION)
        self.config.set(SECTION, 'proxy_address', proxy_address)
        self.config.set(SECTION, 'port', str(port))

        if discord_place == "":
            self.config.set(SECTION, 'discord_place',
                            find_discord_entry_command())
        else:
            self.config.set(SECTION, 'discord_place', None)

    def reset(self):
        self.config.set(SECTION, 'proxy_address', None)
        self.config.set(SECTION, 'port', None)
        self.config.set(SECTION, 'discord_place', find_discord_entry_command())

    def save(
        self,
        proxy_address, port, discord_place
    ):
        validate_setting(proxy_address, port, discord_place)
        self.config.set(SECTION, 'proxy_address', proxy_address)
        self.config.set(SECTION, 'port', port)
        self.config.set(SECTION, 'discord_place', discord_place)
        with open(self.config_place, 'w') as file:
            self.config.write(file)

    def load(self):
        self.config.read(self.config_place)

    @property
    def proxy_address(self):
        return self.config.get(SECTION, "proxy_address")

    @property
    def port(self):
        return self.config.get(SECTION, "port")

    @property
    def discord_place(self):
        return self.config.get(SECTION, "discord_place")

