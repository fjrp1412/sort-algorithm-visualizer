import colors
from time import sleep


def merge(start, end, mid, array):
    aux_array = []
    left_pointer = start
    right_pointer = mid+1

    for i in range(start, end+1):
        if left_pointer > mid:
            aux_array.append(array[right_pointer])
            right_pointer += 1

        elif right_pointer > end:
            aux_array.append(array[left_pointer])
            left_pointer += 1

        elif array[left_pointer] < array[right_pointer]:
            aux_array.append(array[left_pointer])
            left_pointer += 1

        else:
            aux_array.append(array[right_pointer])
            right_pointer += 1

    for i in range(len(aux_array)):
        array[start] = aux_array[i]
        start += 1


def merge_sort(canvas, draw_data, start, end, array, speed):
    if start < end:
        mid = (start + end) // 2
        merge_sort(canvas, draw_data, start, mid, array, speed)
        merge_sort(canvas, draw_data, mid+1, end, array, speed)
        merge(start, end, mid, array)
        array_colors = []

        for i in range(len(array)):
            if i >= start and i < mid:
                array_colors.append(colors.CYAN)

            elif i > start and i <= end:
                array_colors.append(colors.RED)

            elif i == mid:
                array_colors.append(colors.YELLOW)

            else:
                array_colors.append(colors.BLUE)

        draw_data(canvas, array, array_colors)
        sleep(speed)
