import colors
from time import sleep


def bubble_sort(canvas, draw_data, array, speed):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                colors_array = [colors.GREEN if x == j or x ==
                                j+1 else colors.BLUE for x in range(len(array))]

                sleep(speed)
                draw_data(canvas, array, colors_array)
