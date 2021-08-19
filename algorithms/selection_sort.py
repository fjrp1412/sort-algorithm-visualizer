from time import sleep
import colors


def selection_sort(canvas, draw_data, array, time):
    for i in range(len(array)-1):
        minimun_item_index = i
        colors_array = list()

        for j in range(i+1, len(array)):
            if array[j] < array[minimun_item_index]:
                minimun_item_index = j

        sleep(time)
        draw_data(canvas, array, [colors.RED if idx == i else colors.GREEN if idx ==
                  minimun_item_index else colors.BLUE for idx in range(len(array))])

        array[i], array[minimun_item_index] = array[minimun_item_index], array[i]
