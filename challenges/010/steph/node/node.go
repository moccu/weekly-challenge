package node


import (
	"errors"
	"fmt"
)


type Node struct {
	Key int `json:"key"`
	Payload interface{} `json:"payload"`
	Left *Node `json:"left"`
	Right *Node `json:"right"`
}


func New(key int, payload interface{}) *Node {
	return &Node{Key: key, Payload: payload}
}


func (node *Node) String() string {
	return fmt.Sprintf(
		"<Node key:%d (%s) left:%s/right:%s>",
		node.Key,
		node.Payload,
		node.Left,
		node.Right)
}


func (node *Node) Insert(key int, payload interface{}) (*Node, error) {
	if (key == node.Key) {
		return nil, errors.New("New key equals node key.")
	}

	if (key < node.Key) {
		if (node.Left != nil) {
			return node.Left.Insert(key, payload)
		}

		node.Left = New(key, payload)
		return node.Left, nil
	}

	if (node.Right != nil) {
		return node.Right.Insert(key, payload)
	}
	node.Right = New(key, payload)
	return node.Right, nil
}


func (node *Node) LookupNode(key int) (*Node, error) {
	if (key == node.Key) {
		return node, nil
	}

	if (key < node.Key) {
		if (node.Left != nil) {
			return node.Left.LookupNode(key)
		}
		return nil, errors.New("Key not found.")
	}

	if (node.Right != nil) {
		return node.Right.LookupNode(key)
	}
	return nil, errors.New("Key not found.")
}


func (node *Node) Lookup(key int) (interface{}, error) {
	node, err := node.LookupNode(key)
	if (err != nil) {
		return nil, err
	}

	return node.Payload, nil
}
