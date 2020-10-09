class ProxySetting:
    def __init__(self, proxy_address: str, port: int):
        self.proxy_address: str = proxy_address
        self.port: int = port

def load_default_config() -> ProxySetting:
    print("Default config loaded")
    return ProxySetting("example.com", 22)

def launch_discord(proxy_setting: ProxySetting):
    print("Discord launched")

def save_default_setting(proxy_setting: ProxySetting):
    print("Setting saved")
