from typing import List
from tkinter import *
from tkinter.ttk import *

from version import VERSION
from src.view import utils
from src.model.config_object import ConfigObject
from src.controller.validate import validation
from src.controller.start_discord import start_discord


class MainPage:
    def __init__(self, r: Tk):
        self.frame = Frame(r)
        self.root = r

        self.config = ConfigObject()

        PROXY_DESCRIPTION = "HTTPプロキシ:"
        PORT_DESCRIPTION = "ポート番号:"
        PLACE_DESCRIPTION = "Discordの場所:"
        VERSION_DESCRIPTION = "Ver: {}   ".format(VERSION)

        # ラベル
        proxy_label = Label(self.frame, text=PROXY_DESCRIPTION)
        port_label = Label(self.frame, text=PORT_DESCRIPTION)
        place_label = Label(self.frame, text=PLACE_DESCRIPTION)
        version_label = Label(self.frame, text=VERSION_DESCRIPTION, foreground="gray")

        # 入力BOX
        proxy_entry = Entry(self.frame, width=60)
        proxy_entry.insert(END, self.config.proxy_address)
        port_entry = Entry(self.frame, width=8)
        port_entry.insert(END, self.config.port_str)
        place_entry = Entry(self.frame, width=60)
        place_entry.insert(END, self.config.discord_place)

        # 起動ボタン
        self.entries: List[Entry] = [proxy_entry, port_entry, place_entry]
        start_button = Button(self.frame, text="起動", command=self.start_button_command)

        # 配置
        proxy_label.pack()
        proxy_entry.pack()
        port_label.pack()
        port_entry.pack()
        place_label.pack()
        place_entry.pack()
        utils.space(self.frame, 1)
        start_button.pack()
        utils.space(self.frame, 1)
        version_label.pack(anchor="se")

        self.frame.grid(row=0, column=0, sticky="nsew")

    def start_button_command(self):
        law_inputs: List[str] = [entry.get() for entry in self.entries]

        if validation(law_inputs):
            proxy = law_inputs[0]
            port = int(law_inputs[1])
            place = law_inputs[2]
            self.config.set(proxy, port, place)

            start_discord(self.config)
            return

        return
