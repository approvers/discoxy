import platform
import os

import utils
from exceptions import InvalidPlatformError, DiscordNotFoundError

OS_ENVIRONMENT_PATH = {
    "setting":{
        "Windows": utils.get_env_or("APPDATA", "__INVALID_PLATFORM__") + "\\approvers\\discoxy\\",
        "Darwin": utils.get_env_or("HOME", "__INVALID_PLATFORM__") + "/.config/approvers/discoxy/",
        "Linux": utils.get_env_or("HOME", "__INVALID_PLATFORM__") + "/.config/approvers/discoxy/"
    },
    "discord": {
        "Windows": {
            "Path": utils.get_env_or("APPDATA", "__INVALID_PLATFORM__") + "\\Local\\Discord\\Update.exe",
            "Option": "-a=--proxy-server="
        },
        "Darwin": {
            "Path": "/Applications/Discord.app/Contents/MacOS/Discord",
            "Option": "--proxy-server="
        },
        "Linux": {
            "Option": "--proxy-server="
        }
    }
}

def find_discord_entry_command():
    platform_name = platform.system()
    if platform_name not in OS_ENVIRONMENT_PATH["discord"].keys():
        raise InvalidPlatformError(platform_name)
    
    if "Path" not in OS_ENVIRONMENT_PATH["discord"][platform_name].keys():
        raise DiscordNotFoundError("(cannot infer)")
    
    expected_path = OS_ENVIRONMENT_PATH["discord"][platform_name]["Path"]
    if not os.path.isfile(expected_path):
        raise DiscordNotFoundError(expected_path)

    return expected_path
    
print(find_discord_entry_command())
