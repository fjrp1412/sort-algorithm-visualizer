import colors
from time import sleep


def build_max_heap(array, limit, canvas, draw_data, speed):
    last_parent = (limit-1) // 2

    for i in range(last_parent, -1, -1):
        heapify(array, i, limit)

    array[0], array[limit] = array[limit], array[0]


def heapify(array, n, limit):
    left_children = n*2+1
    right_children = n*2+2
    max = n

    if left_children <= limit and array[left_children] > array[max]:
        max = left_children

    if right_children <= limit and array[right_children] > array[max]:
        max = right_children

    if max != n:
        array[n], array[max] = array[max], array[n]


def heap_sort(canvas, draw_data, speed, array):
    for i in range(len(array)-1, 0, -1):
        build_max_heap(array, i, canvas, draw_data, speed)
        sleep(speed)
        draw_data(canvas, array, [colors.GREEN if j >=
                  i else colors.BLUE for j in range(len(array))])
