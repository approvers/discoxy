import subprocess
import platform

from src.model.config_object import ConfigObject
from src.model.discord_entry import OS_ENVIRONMENT_PATH


def start_discord(config: ConfigObject):
    config.save_to_file()
    option = OS_ENVIRONMENT_PATH["discord"][platform.system()]["Options"].format(config.proxy_address, config.port_str)

    print(config.discord_place, option)

    command = [config.discord_place, option]
    subprocess.run(command)

    return
