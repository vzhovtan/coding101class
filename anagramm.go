//Find if two given strings are anagramms
package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	// commands args option
	s1 := os.Args[1]
	s2 := os.Args[2]
	fmt.Println(anagramm(s1, s2))
}

func anagramm(s1, s2 string) bool {
	if len(s1) != len(s2) {
		return false
	}
	for _, v := range s1 {
		if !strings.Contains(s2, string(v)) {
			return false
		}
	}
	return true
}
