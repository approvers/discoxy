import os
from typing import Optional
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from urllib import parse

from lib import controller

PROGRAM_NAME: str = "discoxy"


class Root:
    def __init__(self):
        self.window = Tk()
        self.window.title(PROGRAM_NAME)
        self.window.geometry("450x200")
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        main_page = MainPage(self.window)

        main_page.frame.tkraise()

        self.window.mainloop()


class MainPage:
    def __init__(self, r: Tk):
        """
        Args:
            r(tk.Tk): tk.Tk()で取得できるwindow
        """
        self.frame = Frame(r)
        self.root = r

        PROXY_DESCRIPTION = "HTTPプロキシ:"
        PORT_DESCRIPTION = "ポート番号:"
        PLACE_DESCRIPTION = "Discordの場所"

        proxy_label = Label(self.frame, text=PROXY_DESCRIPTION)
        port_label = Label(self.frame, text=PORT_DESCRIPTION)
        place_label = Label(self.frame, text=PLACE_DESCRIPTION)

        self.proxy_entry = Entry(self.frame)
        self.proxy_entry.insert(END, "")
        self.port_entry = Entry(self.frame)
        self.port_entry.insert(END, "")
        self.place_entry = Entry(self.frame, width=40)
        self.place_entry.insert(END, "")

        start_button = Button(self.frame, text="起動", command=self.start)

        proxy_label.pack()
        self.proxy_entry.pack()
        port_label.pack()
        self.port_entry.pack()
        place_label.pack()
        self.place_entry.pack()
        Utils.space(self.frame, 1)
        start_button.pack()

        self.frame.grid(row=0, column=0, sticky="nsew")

    def start(self):
        self.parser(self.proxy_entry.get(), self.place_entry.get(), self.port_entry.get())

    def parser(self, law_proxy: str, law_place: str, law_port: str):
        if not Utils.is_url(law_proxy):
            Utils.error_dialog("Invalid address has passed. Please specify valid URL.")
            return

        try:
            port = int(law_port)
        except Exception as e:
            Utils.error_dialog(e)
            return

        if not (0 <= port <= 65535):
            Utils.error_dialog("Invalid port number has passed. Please specify within 0 ~ 65535.")
            return

        try:
            if not os.path.exists(law_place):
                raise FileNotFoundError("File not found. Please check your file.")
        except Exception as e:
            Utils.error_dialog(e)
            return

        DataClass.law_proxy = str(self.proxy_entry.get())
        DataClass.law_place = str(self.place_entry.get())
        DataClass.law_port = int(self.port_entry.get())


class Utils:
    @staticmethod
    def space(frame: Frame, count: int):
        for _ in range(count):
            Label(frame, text="").pack()

    @staticmethod
    def is_url(text):
        url_param = parse.urlparse(text)
        return len(url_param.scheme) > 0

    @staticmethod
    def error_dialog(message: str):
        showerror(message=message)


class DataClass:
    law_proxy: Optional[str] = None
    law_port: Optional[int] = None
    law_place: Optional[str] = None
