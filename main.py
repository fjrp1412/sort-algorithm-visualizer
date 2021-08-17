# Tabnine::sem
import tkinter as tk
from tkinter import ttk
import random

CANVAS_WIDTH = 900
CANVAS_HEIGHT = 400
SORTS_ARRAY = ["Bubble Sort", "Quick Sort", "Merge Sort",
               "Insertion Sort", "Heap Sort", "Counting Sort", "Selection Sort"
               ]
root = tk.Tk()
root.config(bg="#fff")
root.maxsize(1000, 900)


def hello_world():
    print("Hello world")


def draw_data(canvas):
    canvas.delete("all")
    array = [random.randint(1, 100) for i in range(200)]
    max_number = max(array)
    normalize = [x/max_number for x in array]
    spacing = 15
    x_width = CANVAS_WIDTH / (len(array) + 1)

    for i, height in enumerate(normalize):
        x0 = i * x_width + spacing
        y0 = CANVAS_HEIGHT - height * 400
        x1 = (i + 1) * x_width + 15
        y1 = CANVAS_HEIGHT
        canvas.create_rectangle(x0, y0, x1, y1, fill="#0ca8f6")

    root.update_idletasks()


def run():
    ui = tk.Frame(root, bg="#fff", width=900, height=300)
    ui.grid(row=0, column=0, padx=10, pady=5)

    label_algorithms = tk.Label(ui, text="Choose Algorithm: ", bg="#fff")
    label_algorithms.grid(row=0, column=0)
    menu_algorithms = ttk.Combobox(ui, textvariable=tk.StringVar(), values=SORTS_ARRAY, state="readonly")
    menu_algorithms.grid(row=0, column=1, padx=5, pady=5)
    menu_algorithms.current(0)

    label_time = tk.Label(ui, text="Choose sort speed: ", bg="#fff")
    label_time.grid(row=1, column=0)
    menu_speed = ttk.Combobox(ui, textvariable=tk.StringVar(), values=[
                              "Slow", "Normal", "Fast"], state="readonly")
    menu_speed.grid(row=1, column=1)
    menu_speed.current(0)

    button_array = tk.Button(ui, text="Generate Array",
                             command=lambda: draw_data(canvas))
    button_array.grid(row=2, column=0)

    button_start = tk.Button(ui, text="Start sort")
    button_start.grid(row=2, column=1)

    canvas = tk.Canvas(root, width=CANVAS_WIDTH,
                       height=CANVAS_HEIGHT, bg="#fff")
    canvas.grid(row=1, column=0, padx=15, pady=5)

    root.mainloop()


if __name__ == '__main__':
    run()
