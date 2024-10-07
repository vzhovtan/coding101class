'''
Code examples with sliding window fixed and variable size
https://tproger.ru/translations/14-templates-to-answer-interview-questions/
'''

# max sub-array size k sum (easy)
def max_sub(arr, k):
  larg = 0
  for i in range(len(arr)+1-k):
    larg  = max(larg, sum(arr[i:i+k]))
  return larg

# longest sub-string with the same chars (medium)
def longest_sub_same(arr):
  longest = 0
  for i in range(len(arr)):
    curr_long = 1
    for j in range(i, len(arr)-1):
      if arr[j+1] == arr[j]:
        curr_long +=1
      else:
        break
    longest = max(longest, curr_long)
  return longest

# longest sub-string with the all different chars (medium)
def longest_sub_dif(arr, k):
  longest = ""
  for i in range(len(arr)):
    curr_long = ""
    for j in range(i, len(arr)):
      if len(set(arr[i:j+1])) > k:
        curr_long = arr[i:j]
        break
      else:
        curr_long = arr[i:j+1]
    if len(longest) < len(curr_long):
      longest = curr_long
      # print("current longest", longest)
  return longest
