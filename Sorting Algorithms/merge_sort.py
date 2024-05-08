def merge_sort(merge_list):
    if len(merge_list) > 1:
        mid = int(len(merge_list)/2)
        left_half = merge_list[:mid]

        right_half = merge_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)
        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                merge_list[k] = left_half[i]
                i += 1
            else:
                merge_list[k] = right_half[j]
                j += 1

            k += 1
        while i < len(left_half):

            merge_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):

            merge_list[k] = right_half[j]
            j += 1
            k += 1


array = [5, 3, 2, 7, 9, 1, 3, 8, 3]
merge_sort(array)
print(array)

