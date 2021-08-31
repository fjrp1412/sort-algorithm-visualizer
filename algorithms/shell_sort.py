import random
from time import sleep
import colors


def shell_sort(canvas, draw_data, speed, array):
    k = (len(array)) // 2
    array_blues = [colors.BLUE for i in range(len(array))]
    colors_array = array_blues.copy()
    while k > 0:
        for i in range(k, len(array)):
            temp = array[i]
            j = i

            while j >= k and array[j - k] > temp:

                array[j], array[j-k] = array[j-k], array[j]
                colors_array[j], colors_array[j-k] = colors.RED, colors.RED
                draw_data(canvas, array, colors_array)
                j -= k

            colors_array[i], colors_array[j] = colors.GREEN, colors.GREEN
            sleep(speed)
            draw_data(canvas, array, colors_array)
            colors_array = array_blues.copy()
            array[j] = temp

        k = k // 2


if __name__ == "__main__":
    array = [random.randint(1, 10) for i in range(10)]
    print(array)
    shell_sort(array)
    print(array)
