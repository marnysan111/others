package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	b := true
	scanner := bufio.NewScanner(os.Stdin)

	for b {
		b = scanner.Scan()
		t := scanner.Text()
		fmt.Printf("%v, %s\n", b, t)
		if t == "a" {
			break
		}
	}
}
