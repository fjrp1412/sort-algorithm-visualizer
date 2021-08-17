# Tabnine::sem
import tkinter as tk
from tkinter import ttk
import random
import colors
from algorithms.bubble_sort import bubble_sort
from algorithms.merge_sort import merge_sort
from algorithms.insertion_sort import insertion_sort
from time import sleep

CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 600
SORTS_ARRAY = ["Bubble Sort", "Quick Sort", "Merge Sort",
               "Insertion Sort", "Heap Sort", "Counting Sort", "Selection Sort"
               ]
root = tk.Tk()
root.config(bg="#fff")


def generate_array(canvas, size):
    global array
    array = [random.randint(1, 100) for i in range(size)]
    draw_data(canvas, array, [colors.BLUE for i in range(len(array))])


def draw_data(canvas, array, rectangle_colors):
    canvas.delete("all")
    max_number = max(array)
    normalize = [x/max_number for x in array]
    spacing = 20
    x_width = CANVAS_WIDTH / (len(array) + 1)

    for i, height in enumerate(normalize):
        x0 = i * x_width + spacing
        y0 = CANVAS_HEIGHT - height * 400
        x1 = (i + 1) * x_width + spacing
        y1 = CANVAS_HEIGHT
        canvas.create_rectangle(x0, y0, x1, y1, fill=rectangle_colors[i])

    root.update_idletasks()


def speed_time(option_list):
    speed = option_list.get()
    if speed == "Slow":
        speed = 0.3
    elif speed == "Normal":
        speed = 0.1
    else:
        speed = 0.01
    return speed


def sort_start(canvas, array, option, speed):
    if option == "Bubble Sort":
        bubble_sort(canvas, draw_data, array, speed)

    if option == "Merge Sort":
        merge_sort(canvas, draw_data, 0, len(array)-1, array, speed)

    if option == "Insertion Sort":
        insertion_sort(canvas, draw_data, array, speed)

    sleep(0.5)
    draw_data(canvas, array, [colors.GREEN for i in range(len(array))])


def run():
    ui = tk.Frame(root, bg="#fff", width=900, height=300)
    ui.grid(row=0, column=0, padx=10, pady=5)

    label_algorithms = tk.Label(ui, text="Choose Algorithm: ", bg="#fff")
    label_algorithms.grid(row=0, column=0)
    menu_algorithms = ttk.Combobox(
        ui, textvariable=tk.StringVar(), values=SORTS_ARRAY, state="readonly")
    menu_algorithms.grid(row=0, column=1, padx=5, pady=5)
    menu_algorithms.current(0)

    label_time = tk.Label(ui, text="Choose sort speed: ", bg="#fff")
    label_time.grid(row=1, column=0)

    menu_speed = ttk.Combobox(ui, textvariable=tk.StringVar(), values=[
                              "Slow", "Normal", "Fast"], state="readonly")
    menu_speed.grid(row=1, column=1)
    menu_speed.current(0)

    button_array = tk.Button(ui, text="Generate Array",
                             command=lambda: generate_array(canvas, int(array_size.get())))

    button_array.grid(row=2, column=0)

    button_start = tk.Button(ui, text="Start sort",
                             command=lambda: sort_start(canvas, array, menu_algorithms.get(), speed_time(menu_speed)))

    button_start.grid(row=2, column=1)

    label_array_size = tk.Label(ui, text="Insert the size of array:")
    array_size = tk.Entry(ui)
    label_array_size.grid(row=2, column=2)
    array_size.grid(row=2, column=3)

    canvas = tk.Canvas(root, width=CANVAS_WIDTH,
                       height=CANVAS_HEIGHT, bg="#fff")

    canvas.grid(row=1, column=0, padx=15, pady=5)

    root.mainloop()


if __name__ == '__main__':
    run()
