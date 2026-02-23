from dataclasses import dataclass
from typing import Any, Optional

@dataclass
class Node:
    value: Any 
    left: Optional["Node"] = None
    right: Optional["Node"] = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value: Any) -> bool:
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if temp.value == new_node.value:
                return False
            if new_node.value > temp.value:
                if not temp.right:
                    temp.right = new_node
                    return True
                temp = temp.right
            else:
                if not temp.left:
                    temp.left = new_node
                    return True
                temp = temp.left

    def contains(self, value: Any) -> bool:
        temp = self.root
        while temp is not None:
            if value > temp.value:
                temp = temp.right
            elif value < temp.value:
                temp = temp.left
            else:
                return True
        return False

    def rcontains(self, value):
        def check(node, value):
            if node == None:
                return False
            if value > node.value:
                return check(node.right, value)
            elif value < node.value:
                return check(node.left, value)
            else:
                return True

        return check(self.root, value) 

    def rinsert(self, value):
        if not self.root:
            self.root = Node
        self.__rinsert(self.root, value)

    def __rinsert(self, current_node: Node, value: int):
        if current_node == None: # current node
            return Node(value=value)
        if current_node.value > value:
            current_node.right = self.__rinsert(current_node.right, value)
        if current_node.value < value:
            current_node.left = self.__rinsert(current_node.left, value)
        return current_node # !!!

    def min_value(self, root):
        current_node = root
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def delete_node(self, value):
        self.__delete(self.root, value)

    def __delete(self, current_node, value):
        if current_node == None:
            return None
        elif current_node.value > value:
            current_node.left = self.__delete(current_node.left, value) # !!!
        elif current_node.value < value:
            current_node.right = self.__delete(current_node.right, value) # !!!
        else:
            if current_node.left == None and current_node.right == None:
                return None # !!!
            elif current_node.left == None: # !!!
                current_node = current_node.right
            elif current_node.right == None: # !!!
                current_node = current_node.left
            else:
                min_val = self.min_value(current_node.right)
                current_node.value = min_val
                current_node.right = self.__delete(current_node.right, min_val) #!!!
        return current_node


my_tree = BinarySearchTree()
my_tree.rinsert(47)
my_tree.rinsert(21)
my_tree.rinsert(76)
my_tree.rinsert(18)
my_tree.rinsert(27)
my_tree.rinsert(52)
my_tree.rinsert(82)

print('BST Contains 27:')
print(my_tree.rcontains(27))

print('\nBST Contains 17:')
print(my_tree.rcontains(17))
                


"""
    EXPECTED OUTPUT:
    ----------------
    BST Contains 27:
    True

    BST Contains 17:
    False

"""