package main

import (
	"fmt"
	"io/ioutil"
	"log"
)

type Person struct {
	Id   int    `json:"id"`
	Name string `json:"name"`
	Age  int    `json:"age"`
}

func json() {
	// JSONファイル読み込み
	bytes, err := ioutil.ReadFile("./vro.json")
	if err != nil {
		log.Fatal(err)
	}
	// JSONデコード
	var persons []Person
	if err := json.Unmarshal(bytes, &persons); err != nil {
		log.Fatal(err)
	}
	// デコードしたデータを表示
	for _, p := range persons {
		fmt.Printf("%d : %s\n", p.Id, p.Name)
	}
}
