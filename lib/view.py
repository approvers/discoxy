from tkinter import *
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

        self.proxy_entry = Entry(self.frame)
        self.proxy_entry.insert(END, "")
        self.port_entry = Entry(self.frame)
        self.port_entry.insert(END, "")
        self.place_entry = Entry(self.frame)
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
        law_proxy: str = str(self.proxy_entry.get())
        law_port: int = int(self.port_entry.get())
        law_place: str = str(self.place_entry.get())

        print(law_place, law_port, law_proxy)


class Utils:
    @staticmethod
    def space(frame: Frame, count: int):
        for _ in range(count):
            Label(frame, text="").pack()
