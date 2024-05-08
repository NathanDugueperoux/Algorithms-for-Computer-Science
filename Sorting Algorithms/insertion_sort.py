def insertion_sort(array):
  for i in range(1, len(array)-1):
    elem = array[[i]
    j = i - 1 
    while j > 0 and array[j] > elem:
        array[j+1] = array[j]
        j = j - 1
    array[j + 1] = elem  
