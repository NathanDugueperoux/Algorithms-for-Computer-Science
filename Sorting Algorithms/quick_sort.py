def partition(array: list, start, end):
    pivot = array[end]
    right_mark = end - 1
    left_mark = start
    done = False
    while done == False:
        while right_mark >= left_mark and array[right_mark] >= pivot:
            right_mark -= 1
        while array[left_mark] >= pivot and left_mark <= right_mark:
            left_mark += 1