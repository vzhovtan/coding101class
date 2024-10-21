package coding101class

import (
	"testing"
	"slices"
	"coding101class"
)

func TestFindMaxActivities (t *testing.T){
	start := []int{1, 3, 0, 5, 8, 5}
  fin := []int{2, 4, 6, 7, 9, 9}
	want := []int{1, 3, 5, 8}
	got := coding101class.FindMaxActivities(start, fin)
	if !slices.Equal(want, got) {
		t.Errorf("Test is failing for FindMaxActivities cuntions. Exected %v, got %v", want, got)
	}
}