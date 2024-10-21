/* 
	Return a maximum set of activities that can be done by a single person, one at a time, listed by starting time
  The following implementation assumes that the activities are already sorted according to their finish time
  - start[] - An array that contains start time of all activities
  - fin[] - An array that contains finish time of all activities
*/

package coding101class

func FindMaxActivities(start, fin []int) []int {
	result := []int{}
	// The first activity is always selected
	i := 0
	result = append(result, start[i])
	// For the rest of the activities, if this activity has start time greater than or equal
	// to the finish time of previously selected activity, then select it
	for j := range fin {
		if start[j] >= fin[i] {
			result = append(result, start[j])
			i = j
		}
	}
	return result
}
