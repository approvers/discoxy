import os
import platform
import subprocess

from lib.model import utils


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
            "Path": utils.get_env_or("USERPROFILE", "__INVALID_PLATFORM__") + "\\AppData\\Local\\Discord\\Update.exe",
            "Option": "-a=--proxy-server={}:{}"
        },
        "Darwin": {
            "Path": "/Applications/Discord.app/Contents/MacOS/Discord",
            "Option": "--proxy-server={}:{}"
        },
        "Linux": {
            "Option": "--proxy-server={}:{}"
        }
    }
}

infer_linux_path()


def find_discord_entry_command():
    platform_name = platform.system()
    if platform_name not in OS_ENVIRONMENT_PATH["discord"].keys():
        return None

    if "Path" not in OS_ENVIRONMENT_PATH["discord"][platform_name].keys():
        return None

    expected_path = OS_ENVIRONMENT_PATH["discord"][platform_name]["Path"]

    if not os.path.isfile(expected_path):
        return None

    return expected_path


print(f"Debug: discord_entry:61: {find_discord_entry_command()}")
