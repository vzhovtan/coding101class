"""
Prints a maximum set of activities that can be done by a single person, one at a time
The following implementation assumes that the activities are already sorted according to their finish time
- start[] - An array that contains start time of all activities
- fin[] - An array that contains finish time of all activities
""" 

def findMaxActivities(start, fin: list) -> None: 
  n = len(fin) 
  print("The following activities are selected (starting time)")
  # The first activity is always selected 
  i = 0
  print(start[i]) 
  # Check rest of the activities 
  for j in range(n): 
    # If this activity has start time greater than or equal to the finish time of previously 
  	# selected activity, then select it, for debugging use print(i, j) 
    if start[j] >= fin[i]: 
      print(start[j]) 
      i = j

# driver code
if __name__ == "__main__":
	start = [1, 3, 0, 5, 8, 5] 
	fin = [2, 4, 6, 7, 9, 9] 
	findMaxActivities(start, fin)