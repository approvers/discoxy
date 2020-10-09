import sys

from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *

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
        place_entry = Entry(self.frame)
        place_entry.insert(END, "")

        start_button = Button(self.frame, text="起動", command=self.start)

        proxy_label.pack()
        proxy_entry.pack()
        port_label.pack()
        port_entry.pack()
        place_label.pack()
        place_entry.pack()
        Utils.space(self.frame, 1)
        start_button.pack()

        self.frame.grid(row=0, column=0, sticky="nsew")

    def start(self):
        print("test")


class Utils:
    @staticmethod
    def space(frame: Frame, count: int):
        for _ in range(count):
            Label(frame, text="").pack()


if __name__ == "__main__":
    Root()
