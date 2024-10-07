def qsort(arr):
  if len(arr) <2:
    return arr
  pivot = arr[0]  
  less = [i for i in arr[1:] if i <= pivot]
  bigger = [i for i in arr[1:] if i > pivot]
  return qsort(less) + [pivot] + qsort(bigger)  
