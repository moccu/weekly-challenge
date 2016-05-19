# 010: Binary Trees II (Sorted list)

Use your binary tree from challenge #010 and write a function that returns a sorted list of node-keys.

---
```python

class Node:
    key = None
    data = None
    left_child = None
    right_child = None

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def insert(self, key, value):
        if self.key == key:
            return False

        if self.key > key:
            if self.left_child:
                return self.left_child.insert(key, value)
            else:
                self.left_child = Node(key, value)
                return True
        else:
            if self.right_child:
                return self.right_child.insert(key, value)
            else:
                self.right_child = Node(key, value)
                return True

    def find(self, key):
        if self.key == key:
            return self

        if self.left_child and self.key > key:
            return self.left_child.find(key)

        if self.right_child and self.key < key:
            return self.right_child.find(key)

        return None

    def get_node_list(self, node):
        node_list = []
        if node.left_child:
            node_list += self.get_node_list(node.left_child)

        node_list.append(node.key)

        if node.right_child:
            node_list += self.get_node_list(node.right_child)

        return node_list


class Tree:
    root = None

    def __init__(self, root_key, root_value):
        self.root = Node(root_key, root_value)

    def insert(self, key, value):
        return self.root.insert(key, value)

    def find(self, key):
        return self.root.find(key)

    def get_sorted_list(self):
        sorted_list = self.root.get_node_list(node=self.root)

        return sorted_list


```
From: Ben | Language: Python

---
