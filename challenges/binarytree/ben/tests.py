import pytest
from binarytree import Node


class TestNode:

    def test_init(self):
        node = Node(3, 'value')

        assert node.key == 3
        assert node.value == 'value'

    def test_insert_same_key(self):
        node = Node(3, 'value')

        assert node.insert(3, 'value') is False

    def test_insert_no_left_child(self):
        node = Node(3, 'value')

        assert node.left_child is None
        assert node.insert(2, 'left_value') is True
        assert node.left_child is not None
        assert node.left_child.key == 2
        assert node.left_child.value == 'left_value'

    def test_insert_left_child(self):
        node = Node(3, 'value')
        node.insert(2, 'left_value')

        assert node.left_child.left_child is None
        node.insert(1, 'left_child_value')
        assert node.left_child.left_child is not None
        assert node.left_child.left_child.key == 1
        assert node.left_child.left_child.value == 'left_child_value'

    def test_insert_no_right_child(self):
        node = Node(3, 'value')

        assert node.right_child is None
        assert node.insert(4, 'right_value') is True
        assert node.right_child is not None
        assert node.right_child.key == 4
        assert node.right_child.value == 'right_value'

    def test_insert_right_child(self):
        node = Node(3, 'value')
        node.insert(4, 'right_value')

        assert node.right_child.right_child is None
        node.insert(5, 'right_child_value')
        assert node.right_child.right_child is not None
        assert node.right_child.right_child.key == 5
        assert node.right_child.right_child.value == 'right_child_value'

    @pytest.mark.parametrize('node, child_key, child_child_key, search_key', [
        (Node(4, 'a'), 2, 5, 4),
        (Node(4, 'a'), 2, 5, 2),
        (Node(4, 'a'), 2, 5, 5),
    ])
    def test_find_key(self, node, child_key, child_child_key, search_key):
        node.insert(child_key, 'b')
        node.insert(child_child_key, 'c')

        assert node.find(search_key).key == search_key

    @pytest.mark.parametrize('node, child_key, child_child_key, search_key', [
        (Node(4, 'a'), 2, 5, 6),
        (Node(4, 'a'), 2, 5, 3),
        (Node(4, 'a'), None, None, 6),
        (Node(4, 'a'), None, None, 3),
    ])
    def test_key_not_in_node(self, node, child_key, child_child_key, search_key):
        if child_key:
            node.insert(child_key, 'b')

            if child_child_key:
                node.insert(child_child_key, 'c')

        assert node.find(search_key) is None

    def test_get_node_list(self):
        node = Node(4, 'a')
        node.insert(2, 'b')
        node.insert(5, 'c')
        node.insert(1, 'd')
        node.insert(3, 'e')
        node.insert(6, 'f')

        assert node.get_node_list(node) == [1, 2, 3, 4, 5, 6]
