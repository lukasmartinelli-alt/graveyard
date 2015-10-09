package main // import "github.com/rtpp/worker"


import (
	"fmt"

	"github.com/robertkrimen/otto"
)


func main() {
	vm := otto.New()
	vm.Run(`
		abc = 2 + 2;
		console.log("The value of abc is " + abc); // 4
	`)
	value, _ := vm.Get("abc")
	valueInt , _ := value.ToInteger()
	fmt.Printf("abc: %d", valueInt)
}
