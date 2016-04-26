# 010: Binary Trees II (Lookup)

Use your binary tree from challenge #009 and write a function that looks up a certain key and returns the value.

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
            return 'Node with this key already exists'
        elif self.key > key:
            if self.left_child:
                return self.left_child.insert(key, data)
            else:
                self.left_child = Node(key, data)
                return 'New node created'
        else:
            if self.right_child:
                return self.right_child.insert(key, data)
            else:
                self.right_child = Node(key, data)
                return 'New node created'

    def find(self, key):
        if (self.key == key):
            return self
        elif self.key > key:
            if self.left_child:
                return self.left_child.find(key)
            else:
                return 'Node with this key does not exist'
        else:
            if self.right_child:
                return self.right_child.find(key)
            else:
                return 'Node with this key does not exist'

class Tree:

    def __init__(self):
        self.root = None

    def insert(self, key, data):
        if self.root:
            return self.root.insert(key, data)
        else:
            self.root = Node(key, data)
            return 'Root node created'

    def find(self, key):
        if self.root:
            return self.root.find(key)
        else:
            return 'Empty Tree'

my_tree = Tree()


```
From: Ute | Language: Python

---

```haskell
module Tree ( Tree(..)
            , insert
            , fromList
            , lookup
            ) where

import Prelude hiding (lookup)


data Tree k a = EmptyNode | Node k a (Tree k a) (Tree k a) deriving (Show)


insert :: Ord k => k -> a -> Tree k a -> Tree k a
insert key value EmptyNode = Node key value EmptyNode EmptyNode
insert key value (Node k v left right)
    | key == k = Node k value left right
    | key <  k = Node k v (insert key value left) right
    | key >  k = Node k v left (insert key value right)

fromList :: Ord k => [(k,a)] -> Tree k a
fromList = foldr (\ (k,v) -> insert k v) EmptyNode

lookup :: Ord k => k -> Tree k a -> Maybe a
lookup _ EmptyNode = Nothing
lookup key (Node k v left right)
    | key == k = Just v
    | key <  k = lookup key left
    | key >  k = lookup key right
```
From: Andreas | Language: Haskell

---
```go
see subdirectory.
```
From: steph | Language: Go
