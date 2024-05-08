# Recursion

def binary_search(array , target, first, last):
  if last < first:
    return -1
  else:
    midpoint = int((first + last) / 2)
    if array[midpoint] > target:
        return binary_search(array, target, first, midpoint - 1)
    elif array[midpoint] < target:
        return binary_search(array, target, midpoint + 1, last )
    else:
        return midpoint

