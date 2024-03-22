// In the board game, a player has to try to advance through a sequence of positions.
// Each position has a nonnegative integer associated with it, representing the maximum you can advance from that position in one move.
// Write a program which takes an array of integers, where array[i] denotes the maximum you can advance from index,
// and returns whether it is possible to advance to the last index starting from the beginning of the array

package main

import (
	"fmt"
)

func main() {
	arr1 := []int{2, 4, 1, 1, 0, 1, 3}
	arr2 := []int{2, 4, 1, 1, 0, 2, 3}
	fmt.Println(advance(arr1)) // true
	fmt.Println(advance(arr2)) // false
}

func advance(a []int) bool {
	larg := 0
	for i, v := range a {
		larg = mmax(larg, i+v)
		//fmt.Println(len(a)-1, larg, i, v)
		if larg > len(a)-1 {
			return false
		}
		if larg == len(a)-1 {
			break
		}
	}
	return true
}

func mmax(x, y int) int {
	if x > y {
		return x
	}
	return y
}
