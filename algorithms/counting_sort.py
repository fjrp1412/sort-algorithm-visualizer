import colors
from time import sleep


def counting_sort(canvas, draw_data, array, time):
    max_number = max(array)
    counter_array = [0] * (max_number+1)
    copy_array = array.copy()
    colors_array = [colors.BLUE] * len(array)

    for i, number in enumerate(array):
        counter_array[number] += 1
        colors_array[i] = colors.RED
        sleep(time)
        draw_data(canvas, array, colors_array)
        colors_array[i] = colors.BLUE

    aux_index = 0
    for i, count in enumerate(counter_array):
        aux = count
        for j in range(aux):
            array[aux_index] = i
            aux_index += 1

        # This is to improvement the visual performance. To see how the array is sorted but without make it to slow
        sleep(0.01)

        draw_data(canvas, array, colors_array)
