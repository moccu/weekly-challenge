class Node:

    key_list = []

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

    def create_key_list(self):
        if self.left_child:
            self.left_child.create_key_list()

        self.key_list.append(self.key)

        if self.right_child:
            self.right_child.create_key_list()


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

    def create_key_list(self):
        if self.root:
            self.root.create_key_list()
            return self.root.key_list
        else:
            return 'Empty Tree'
