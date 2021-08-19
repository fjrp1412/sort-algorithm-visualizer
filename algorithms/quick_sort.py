import colors
from time import sleep


def partition(array, low, high):
    pivot_index = (high + low) // 2
    pivot = array[pivot_index]
    array[low], array[pivot_index] = pivot, array[low]
    left_wall = low

    for i in range(low+1, high+1):
        if array[i] <= pivot:
            left_wall += 1
            array[left_wall], array[i] = array[i], array[left_wall]

    array[low], array[left_wall] = array[left_wall], array[low]

    return left_wall


def quick_sort(canvas, draw_data, speed, array, start, end):
    if start <= end:
        pivot_location = partition(array, start, end)
        quick_sort(canvas, draw_data, speed, array, start, pivot_location-1)
        quick_sort(canvas, draw_data, speed, array, pivot_location+1, end)
        sleep(speed)
        draw_data(canvas, array, [
                  colors.YELLOW if i == pivot_location else colors.CYAN if i < pivot_location+1 and i >= start else colors.RED if i <= end and i > pivot_location+1 else colors.BLUE for i in range(len(array))])

