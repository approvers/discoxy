from tkinter import *
from tkinter.ttk import *


def space(frame: Frame, count: int):
    for _ in range(count):
        Label(frame, text="").pack()
