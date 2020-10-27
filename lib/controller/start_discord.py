import subprocess
import platform

from lib.model.config_object import ConfigObject
from lib.model.discord_entry import OS_ENVIRONMENT_PATH


def start_discord(config: ConfigObject):
    config.save_to_file()
    option = OS_ENVIRONMENT_PATH["discord"][platform.system()]["Options"].format(config.proxy_address, config.port_str)

    print(config.discord_place, option)

    if platform.system() == "Windows":
        option = option.split()
        command = [config.discord_place, option[0], option[1], option[2]]
        subprocess.run(command)
    else:
        command = [config.discord_place, option]
        subprocess.run(command)

    return


