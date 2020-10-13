from lib.model.proxy_setting import ProxySetting


def load_default_config() -> ProxySetting:
    print("Default config loaded")
    return ProxySetting("example.com", 22)


def launch_discord(proxy_setting: ProxySetting):
    print("Discord launched")


def save_default_setting(proxy_setting: ProxySetting):
    print("Setting saved")
