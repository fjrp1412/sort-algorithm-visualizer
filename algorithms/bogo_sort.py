import colors
from time import sleep
import random


def bogo_sort(canvas, draw_data, array):
    count = 0
    copy_array = sorted(array)
    array_colors = [colors.BLUE] * len(array)
    while copy_array != array:
        count += 1
        for j in range(len(array)):
            random_number = random.randint(0, len(array)-1)
            array[j], array[random_number] = array[random_number], array[j]

        sleep(0.1)
        draw_data(canvas, array, array_colors)


if __name__ == "__main__":
    array = [4, 3, 2, 1, 5]
    bogo_sort(array)
