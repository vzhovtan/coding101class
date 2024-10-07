'''
Code examples with two pointers
https://tproger.ru/translations/14-templates-to-answer-interview-questions/
'''

# found all pairs with sum equal to k (easy)
def pair_sum(arr, k):
  res = []
  for i in range(len(arr)):
    for j in range(len(arr)-1, i, -1):
      if arr[i] + arr[j] < k:
        break
      elif arr[i] +arr[j] > k:
        continue
      res.append((arr[i], arr[j]))
  return res    


# find all trpilets with sum equal to 0 (medium)
def triplet_zero(arr):
  res = []
  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      for k in range (len(arr)-1, j, -1):
        if arr[i] + arr[j] == -arr[k]:
          res.append((arr[i], arr[j], arr[k]))
  return res