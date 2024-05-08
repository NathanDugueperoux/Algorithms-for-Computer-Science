def linear_search(item_sought, array: list):
    found = False
    index = -1
    i = 0
    while i < len(array) and found == False:
        if array[i] == item_sought:
            index = i
            found = True
        i += 1
    return index
