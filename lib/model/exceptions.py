class InvalidPlatformError(RuntimeError):
    def __init__(self, platform_name: str):
        super().__init__("Invalid platform! Current platform name: \"{0}\"".format(platform_name))
        self.platform_name = platform_name


class DiscordNotFoundError(RuntimeError):
    def __init__(self, expected_path: str):
        super().__init__("Discord not found! Expected path: \"{0}\"".format(expected_path))
        self.expected_path = expected_path


class InvalidParameterError(RuntimeError):
    def __self__(
            self,
            invalid_address: bool,
            invalid_port: bool,
            invalid_path: bool
    ):
        super().__init__("入力された値に誤りがあります: {}".format(self.make_message()))

    def make_message(self):
        status_list = [self.invalid_address, self.invalid_port, self.invalid_path]
        message_list = ["アドレス", "ポート", "Discordの場所"]
        invalid_status = [message_list[x] for x in range(3) if status_list[x]]
        return ", ".join(invalid_status)
