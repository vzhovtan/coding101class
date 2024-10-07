package main

import (
	"fmt"
)

func swap(arr *[]int, idx int) {
	if (*arr)[idx] > (*arr)[idx+1] {
		(*arr)[idx], (*arr)[idx+1] = (*arr)[idx+1], (*arr)[idx]
	}
}

func bubble(inp []int) {
	for j := len(inp) - 1; j >= 0; j-- {
		for i := 0; i < j; i++ {
			swap(&inp, i)
		}
	}
}

func main() {
	arr := []int{1, 9, 2, 8, 3, 7, 4, 6, 5}
	fmt.Println(arr)
	bubble(arr)
	fmt.Println(arr)
}
