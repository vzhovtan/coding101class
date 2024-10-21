package coding101class

import (
	"math"
)

func Sqrt(x float64) float64 {
	z := 1.0
	a := 0.00001
	for math.Abs(x-z*z) > a {
		z += (x - z*z) / (2 * z)
		// fmt.Println(z)
	}
	return z
}
