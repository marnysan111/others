package main

import (
	"fmt"
	"strconv"
)

func fizz() {
	for i := 1; i <= 30; i++ {
		if i%3 == 0 && i%5 == 0 {
			fizz_arr[i] = "FizzBuzz"
		} else if i%3 == 0 {
			fizz_arr[i] = "Fizz"
		} else if i%5 == 0 {
			fizz_arr[i] = "Buzz"
		} else {
			fizz_arr[i] = strconv.Itoa(i)
		}
	}
	fmt.Println(fizz_arr)
}
