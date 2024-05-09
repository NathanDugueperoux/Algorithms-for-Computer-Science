def partition(array: list, start, end):
    pivot = array[end]
    right_mark = end - 1
    left_mark = start
    done = False
    while done == False:
        while right_mark >= left_mark and array[right_mark] > pivot:
            right_mark -= 1
        while array[left_mark] < pivot and left_mark <= right_mark:
            left_mark += 1
        if left_mark < right_mark:
            done = True
        else:
            temp = array[left_mark]
            array[left_mark] = array[right_mark]
            array[right_mark] = temp
    temp = array[start]
    array[start] = array[right_mark]
    return right_mark


def quick_sort(array: list, start, end):
    if start < end:
        split = partition(array, start, end)
        quick_sort(array, start, split-1)
        quick_sort(array, split+1, end)
    return array


nums = [9, 5, 4, 15, 3, 8, 11]
sorted = quick_sort(nums, 0, len(nums)-1)