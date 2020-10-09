import platform

import utils
from exceptions import *

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

