"""
  Return a maximum set of activities that can be done by a single person, one at a time, listed by starting time
  The following implementation assumes that the activities are already sorted according to their finish time
  - start[] - An array that contains start time of all activities
  - fin[] - An array that contains finish time of all activities
""" 

def findMaxActivities(start, fin: list) -> list: 
  n = len(fin) 
  result = []
  # The first activity is always selected 
  i = 0
  result.append(start[i]) 
  # Check rest of the activities 
  for j in range(n): 
    # If this activity has start time greater than or equal to the finish time of previously 
  	# selected activity, then select it, for debugging use print(i, j) 
    if start[j] >= fin[i]: 
      result.append(start[j]) 
      i = j
  return result