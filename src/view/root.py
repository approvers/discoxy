from tkinter import *

from src.view.pages.main import MainPage
from src.model.version_relation import VersionRelation

PROGRAM_NAME: str = "discoxy"


class Root:
    def __init__(self, version_status: VersionRelation):
        self.version_status = version_status

        self.window = Tk()
        self.window.title(PROGRAM_NAME)
        self.window.geometry("420x220")
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

    def run(self):
        main_page = MainPage(self.window, self.version_status)
        main_page.frame.tkraise()

        self.window.mainloop()
