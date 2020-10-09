from functools import partial
from typing import List
from tkinter import *
from tkinter.ttk import *

from lib.model import utils
from lib.model.validation import validation

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
        self.frame = Frame(r)
        self.root = r

        PROXY_DESCRIPTION = "HTTPプロキシ:"
        PORT_DESCRIPTION = "ポート番号:"
        PLACE_DESCRIPTION = "Discordの場所"

        proxy_label = Label(self.frame, text=PROXY_DESCRIPTION)
        port_label = Label(self.frame, text=PORT_DESCRIPTION)
        place_label = Label(self.frame, text=PLACE_DESCRIPTION)

        proxy_entry = Entry(self.frame)
        proxy_entry.insert(END, "")
        port_entry = Entry(self.frame)
        port_entry.insert(END, "")
        place_entry = Entry(self.frame, width=40)
        place_entry.insert(END, "")

        law_inputs: List[str] = [proxy_entry.get(), port_entry.get(), place_entry.get()]
        start_button = Button(self.frame, text="起動", command=partial(self.start_button_command, law_inputs))

        proxy_label.pack()
        proxy_entry.pack()
        port_label.pack()
        port_entry.pack()
        place_label.pack()
        place_entry.pack()
        utils.space(self.frame, 1)
        start_button.pack()

        self.frame.grid(row=0, column=0, sticky="nsew")

    def start_button_command(self, law_inputs: List[str]):
        validation(law_inputs)
