def merge (arr1, arr2):
  res = []
  while arr1 and arr2:
    if arr1[0] <= arr2[0]:
      res.append(arr1[0])
      arr1.pop(0)
    else:
      res.append(arr2[0])
      arr2.pop(0) 
  if arr2:
    res.extend(arr2)  
  elif arr1:
    res.extend(arr1)     
  return res

arr2 = [1, 2, 4, 5, 6]
arr1 = [3, 7, 8, 9, 10]  
print(merge(arr1, arr2))
