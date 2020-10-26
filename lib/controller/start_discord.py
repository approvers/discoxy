from lib.model.config_object import ConfigObject


def start_discord(config: ConfigObject):
    # TODO: ここにDiscordを起動する処理を書いてください
    config.save_to_file()
    exit(0)
