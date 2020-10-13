class Config:
    def __init__(self, proxy_address: str, port: int, discord_place: str):
        self.proxy_address: str = proxy_address
        self.port: int = port

        if discord_place is None or discord_place == "":
            # ここにデフォルトの場所を取得する処理を書く
            pass

        self.discord_place = discord_place
