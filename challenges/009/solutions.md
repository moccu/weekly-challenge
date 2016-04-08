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
