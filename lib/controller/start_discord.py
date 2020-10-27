import subprocess
import platform

from lib.model.config_object import ConfigObject
from lib.model.discord_entry import OS_ENVIRONMENT_PATH


def start_discord(config: ConfigObject):
    config.save_to_file()
    option = OS_ENVIRONMENT_PATH["discord"][platform.system()]["Option"].format(config.proxy_address, config.port_str)
    command = [f"{config.discord_place}", option]
    subprocess.Popen(command)
    return
