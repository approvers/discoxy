from typing import Optional
from tkinter import messagebox

WARNING_TITLE = "Discoxy - 警告"


def warning(content: Optional[str]) -> None:
    messagebox.showwarning(WARNING_TITLE,content)
