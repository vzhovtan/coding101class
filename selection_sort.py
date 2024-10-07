def smallest(arr):
  small_idx = 0
  small = arr[0]
  for i, v in enumerate(arr):
    if v < small:
      small_idx = i
      small = v
  return small_idx

def sel_sort(arr):
  sorted_arr = []
  while len(arr) > 0:
    small_idx = smallest(arr)
    sorted_arr.append(arr.pop(small_idx))
  return sorted_arr 