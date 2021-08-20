from time import sleep
import colors


def insertion_sort(canvas, draw_data, array, speed):
    for i in range(len(array)):
        j = i
        while j > 0 and array[j-1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]
            j -= 1
        sleep(speed)
        draw_data(canvas, array, [
              colors.RED if i == j else colors.GREEN if i == j-1 else colors.BLUE for i in range(len(array))])
