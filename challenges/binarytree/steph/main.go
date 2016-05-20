package main


import (
	"fmt"
	"encoding/json"
	"binarytree/node"
)


func main() {
	tree := node.New(4, "d")

	tree.Insert(2, "b")
	tree.Insert(1, "a")
	tree.Insert(3, "c")
	tree.Insert(5, "e")
	tree.Insert(6, "f")

	data, _ := json.Marshal(tree)
	fmt.Println(string(data[:]))

	fmt.Println(tree.LookupNode(2))
	fmt.Println(tree.LookupNode(3))
	fmt.Println(tree.LookupNode(8))

	fmt.Println(tree.Traverse())
}
