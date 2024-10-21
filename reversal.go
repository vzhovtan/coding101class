//Return reversed given string
package coding101class

import (
	"fmt"
)

func ght() {
	var point, res string
	fmt.Printf("Enter the string \n")
	fmt.Scan(&point)
	for i := len(point) - 1; i >= 0; i-- {
		res += string(point[i])
	}
	fmt.Println(res)
}
