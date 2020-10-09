class InvalidPlatformError(RuntimeError):
    def __init__(self, platform_name: str):
        super().__init__("Invalid platform! Current platform name: \"{0}\"".format(platform_name))
        self.platform_name = platform_name

class DiscordNotFoundError(RuntimeError):
    def __init__(self, expected_path: str):
        super().__init__("Discord not found! Expected path: \"{0}\"".format(expected_path))
        self.expected_path = expected_path

