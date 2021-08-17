import tkinter as tk
from tkinter import ttk
from tkinter import *


def run():
    root = tk.Tk()
    root.geometry("800x800")
    root.config(bg="#fff")
    algorithms_options = ttk.Combobox(root, textvariable=StringVar(), justify="center", values=[
                                      "Bubble Sort", "Selection sort", "Quick sort"], state="readonly")
    algorithms_options.grid(row=0, column=0)
    algorithms_options.current(0)

    root.mainloop()


def menu():
    pass


if __name__ == '__main__':
    run()
