import tkinter as tk


class HelloWorld(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = tk.Label(self, text="Hello World")
        self.label.pack(padx=100, pady=100)


def tkinter_without_poo():
    root = tk.Tk()

    label = tk.Label(root, text="Hello World")
    label.pack(padx=100, pady=100)
    root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    main = HelloWorld(root)
    main.pack(fill="both", expand=True)
    root.mainloop()
