package coding101class

import (
	"testing"
	"coding101class"
)

func TestAnagramm (t *testing.T){
	got := coding101class.Anagramm("hello", "olleh")
	if !got {
		t.Error("got fail for testing anagramm func")
	}
}