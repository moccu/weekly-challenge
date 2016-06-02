from binary_tree import Tree


class TestTree:
    
    def setup(self):
        self.test_tree = Tree()
        self.test_key_4 = 4
        self.test_key_2 = 2
        self.test_key_5 = 5
        self.test_key_3 = 3
        self.test_key_6 = 6
        self.test_key_1 = 1
        
        self.test_data = 'test_data'
    
    def test_insert(self):
        root = self.test_tree.insert(self.test_key_4, self.test_data)
        assert root == 'Root node created'
        
        node = self.test_tree.insert(self.test_key_2, self.test_data)
        assert node == 'New node created'
        
        duplicate_node = self.test_tree.insert(self.test_key_2, self.test_data)
        assert duplicate_node == 'Node with this key already exists'
    
    def test_find_empty_tree(self):
        message = self.test_tree.find(1)
        assert message == 'Empty Tree'
    
    def test_find_does_not_exist(self):
        self.test_tree.insert(self.test_key_4, self.test_data)
        self.test_tree.insert(self.test_key_2, self.test_data)
        self.test_tree.insert(self.test_key_5, self.test_data)
        
        no_node = self.test_tree.find(self.test_key_3)
        assert no_node == 'Node with this key does not exist'
    
    def test_find(self):
        self.test_tree.insert(self.test_key_4, self.test_data)
        self.test_tree.insert(self.test_key_2, self.test_data)
        self.test_tree.insert(self.test_key_5, self.test_data)
        
        root_node = self.test_tree.find(self.test_key_4)
        assert str(root_node) == 'Key: 4'
        left_child = self.test_tree.find(self.test_key_2)
        assert str(left_child) == 'Key: 2'
        right_child = self.test_tree.find(self.test_key_5)
        assert str(right_child) == 'Key: 5'
    
    def test_create_key_list(self):
        self.test_tree.insert(self.test_key_4, self.test_data)
        self.test_tree.insert(self.test_key_2, self.test_data)
        self.test_tree.insert(self.test_key_5, self.test_data)
        self.test_tree.insert(self.test_key_3, self.test_data)
        self.test_tree.insert(self.test_key_6, self.test_data)
        self.test_tree.insert(self.test_key_1, self.test_data)
        expected_result = [1, 2, 3, 4, 5, 6]
        
        result = self.test_tree.create_key_list()
        assert result == expected_result
