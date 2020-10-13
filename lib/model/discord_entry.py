import os
import platform
import subprocess

from lib.model import utils
from lib.model.exceptions import DiscordNotFoundError, InvalidPlatformError


def infer_linux_path():
    global OS_ENVIRONMENT_PATH
    platform_name = platform.system()
    if platform_name != "Linux":
        return
    which_result = subprocess.run(
        ["which", "discord"],
        encoding="utf-8", stdout=subprocess.PIPE
    )
    if which_result.returncode != 0:
        return
    OS_ENVIRONMENT_PATH["discord"]["Linux"]["Path"] = which_result.stdout.strip()

OS_ENVIRONMENT_PATH = {
    "setting": {
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

infer_linux_path()


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
