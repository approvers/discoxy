class ProxySetting:
    def __init__(self, proxy_address: str, port: int):
        self.proxy_address: str = proxy_address
        self.port: int = port