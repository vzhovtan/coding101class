// GCD implementation with flags
package main

import (
	"flag"
	"fmt"
)

var x = flag.Int("1st", 10, "first args")
var y = flag.Int("2nd", 8, "second args")

func main() {
	flag.Parse()
	for *y != 0 {
		*x, *y = *y, *x%*y
	}
	fmt.Println(*x)
}
