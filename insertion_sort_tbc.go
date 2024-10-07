package main

import (
	"fmt"
)

func swapp(arr *[]int, idx int) {
	if (*arr)[idx-1] > (*arr)[idx] {
		(*arr)[idx], (*arr)[idx-1] = (*arr)[idx-1], (*arr)[idx]
	}
}

func insertion(inp []int) {
	for i := 1; i < len(inp); i++ {
		for j := i; j > 0; j-- {
			swapp(&inp, j)
		}
	}
}

func main() {
	arr := []int{1, 9, 2, 8, 3, 7, 4, 6, 5, 3, 4, 5, 6, 1, 2, 2}
	fmt.Println(arr)
	insertion(arr)
	fmt.Println(arr)
}
