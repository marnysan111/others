package main

import (
	"fmt"
	"math/rand"
	"time"
)

func minnum() {
	rand.Seed(time.Now().UnixNano())

	for i := 0; i < 10; i++ {
		min_arr[i] = rand.Intn(50)
	}
	fmt.Println(min_arr)

	min := min_arr[0]
	for j := 0; j < 10; j++ {
		if min_arr[j] < min {
			min = min_arr[j]
		}
	}
	fmt.Println(min)
}
