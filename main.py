import sys
import tkinter


def main():
    root = tkinter.Tk()
    root.title("Discoxy")
    root.geometry("450x200")

    label = tkinter.Label(text="HTTPプロキシ:")
    label.pack()

    edit_box = tkinter.Entry(width=30)
    edit_box.pack()

    label2 = tkinter.Label(text="ポート番号:")
    label2.pack()

    edit_box2 = tkinter.Entry(width=30)
    edit_box2.pack()

    button = tkinter.Button(text="起動", width=10)
    button.bind("<button-1>", None)
    button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
