//Return reversed given string
package main

import (
	"fmt"
)

func main() {
	var point, res string
	fmt.Printf("Enter the string \n")
	fmt.Scan(&point)
	for i := len(point) - 1; i >= 0; i-- {
		res += string(point[i])
	}
	fmt.Println(res)
}
