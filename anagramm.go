//Find if two given strings are anagramms
package coding101class

import (
	"strings"
)

func Anagramm(s1, s2 string) bool {
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
