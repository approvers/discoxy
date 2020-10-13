from lib.model.setting import Config


def load_default_config() -> Config:
    print("Default config loaded")
    return Config("example.com", 22)


def launch_discord(proxy_setting: Config):
    print("Discord launched")


def save_default_setting(proxy_setting: Config):
    print("Setting saved")
