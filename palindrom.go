//Find if given string is palindrom eg: "redivider"
package main

import (
	"fmt"
)

func main() {
	var s1 string
	fmt.Printf("Enter the string \n")
	fmt.Scan(&s1)
	fmt.Println(palindrom(s1, reverse(s1)))
}

func reverse(s string) string {
	var srev string
	for i := len(s) - 1; i >= 0; i-- {
		srev += string(s[i])
	}
	return srev
}

func palindrom(s1, s2 string) bool {
	if len(s1) != len(s2) {
		return false
	}
	for i, v := range s1 {
		if string(v) != string(s2[i]) {
			return false
		}
	}
	return true
}
