# 009: Binary Trees I

A binary tree is a tree data structure in which each node contains a key, a value and at most two other nodes, which are referred to as the left child and the right child. The left node has a smaller key and the right node has a larger key than the node holding them.

Here is an example of a simple tree.

```
    (4)
   /   \
  (2)  (5)
  / \    \
(1) (3)  (6)
```

In JSON this tree could be represented like this:

```javascript
{
	"key": "4",
	"value": "d",
	"left": {
		"key": "2",
		"value": "b",
		"left": {
			"key": "1",
			"value": "a",
			"left": null,
			"right": null
		},
		"right": {
			"key": "3",
			"value": "c",
			"left": null,
			"right": null
		}
	},
	"right": {
		"key": "5",
		"value": "e",
		"left": null,
		"right": {
			"key": "6",
			"value": "f",
			"left": null,
			"right": null
		}
	}
}
```

Write a function that creates a new binary tree from an inital key value pair and another function that inserts new values into an existing binary tree.

---

```python

class Node:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left_child = None
        self.right_child = None

    def insert(self, key, data):
        if self.key == key:
            return False
        elif self.key > key:
            if self.left_child:
                return self.left_child.insert(key, data)
            else:
                self.left_child = Node(key, data)
                return True
        else:
            if self.right_child:
                return self.right_child.insert(key, data)
            else:
                self.right_child = Node(key, data)
                return True

class Tree:

    def __init__(self):
        self.root = None

    def insert(self, key, data):
        if self.root:
            return self.root.insert(key, data)
        else:
            self.root = Node(key, data)
            return True

my_tree = Tree()

my_tree.insert(4, 'd')

```
From: Ute | Language: Python

---

```go
package main

import (
	"errors"
	"fmt"
	"encoding/json"
)


type Node struct {
	Key int `json:"key"`
	Payload interface{} `json:"payload"`
	Left *Node `json:"left"`
	Right *Node `json:"right"`
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
		} else {
			node.Left = NewNode(key, payload)
			return node.Left, nil
		}
	}

	if (node.Right != nil) {
		return node.Right.Insert(key, payload)
	} else {
		node.Right = NewNode(key, payload)
		return node.Right, nil
	}
}


func NewNode(key int, payload interface{}) *Node {
	return &Node{Key: key, Payload: payload}
}


func main() {
	tree := NewNode(4, "d")

	tree.Insert(2, "b")
	tree.Insert(1, "a")
	tree.Insert(3, "c")
	tree.Insert(5, "e")
	tree.Insert(6, "f")

	data, _ := json.Marshal(tree)
	fmt.Println(string(data[:]))
}
```
From: steph | Language: Go

---
```javascript
function BinaryTree(data) {
	this._root = null;
}

BinaryTree.prototype = {
	add: function(data) {
		var
			node = {
				"key": data.key,
				"left": null,
				"right": null
			},
			current
		;

		if (this._root === null) {
			this._root = node;
		} else {
			current = this._root;

			while(true){
				if (data.key < current.key){
					if (current.left === null){
						current.left = node;
						break;
					} else {
						current = current.left;
					}
				} else if (data.key > current.key){
					if (current.right === null){
						current.right = node;
						break;
					} else {
						current = current.right;
					}
				} else {
					break;
				}
			}
		}
	}
}
```
From: Dimitri | Language: Javascript

---

```haskell
data Tree a = EmptyNode | Node String a (Tree a) (Tree a) deriving (Show)

insert :: Tree a -> String -> a -> Tree a
insert EmptyNode key value = Node key value EmptyNode EmptyNode
insert (Node k v left right) key value
	| key == k = Node k value left right
	| key <  k = Node k v (insert left key value) right
	| key >  k = Node k v left (insert right key value)
```
From: Andreas | Language: Haskell

