// Prints a maximum set of activities that can be done by a single person, one at a time
// The following implementation assumes that the activities are already sorted according to their finish time
// - start[] - An array that contains start time of all activities
// - fin[] - An array that contains finish time of all activities

package main

import (
	"fmt"
)

func main() {
	fmt.Println("selected activities (starting time):")
	start := []int{1, 3, 0, 5, 8, 5}
	fin := []int{2, 4, 6, 7, 9, 9}
	// The first activity is always selected
	i := 0
	fmt.Println(start[i])
	// For the rest of the activities, if this activity has start time greater than or equal
	// to the finish time of previously selected activity, then select it
	for j := range fin {
		if start[j] >= fin[i] {
			fmt.Println(start[j])
			i = j
		}
	}
}
