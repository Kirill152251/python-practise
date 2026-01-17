from random import randint
from dataclasses import dataclass

@dataclass
class Node:
    value: int
    next = None 

class LinkedList:
    def __init__(self, value: int) -> None: 
        new_node = Node(value=value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value: int) -> bool:
        new_node = Node(value=value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        return True

    def show(self) -> None:
        values = []
        temp = self.head
        while temp:
            values.append(str(temp.value))
            temp = temp.next
        print(" -> ".join(values))

    def pop(self) -> Node:
        if self.length == 0:
            return None
        temp = pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = self.tail = None
        return temp

    def pop_first(self) -> Node:
        if self.length in (0, 1):
            return self.pop() 
        temp = self.head
        self.head = self.head.next
        self.length -= 1
        temp.next = None
        return temp

    def prepend(self, value: int) -> bool:
        new_node = Node(value=value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def get(self, index: int) -> Node:
        if index < 0 or index >= self.length:
            return None 
        node_to_return = self.head
        for _ in range(index):
            node_to_return = node_to_return.next
        return node_to_return

    def set_value(self, index: int, value: int) -> bool:
        node = self.get(index=index)
        if node:
            node.value = value
            return True
        return False

    def insert(self, index: int, value: int) -> bool:
        if index == 0:
            return self.prepend(value=value)
        if index == self.length:
            return self.append(value=value)
        temp = self.get(index=index)
        if not temp:
            return False
        new_node = Node(value=value)
        pre = self.get(index - 1)
        pre.next = new_node
        new_node.next = temp
        self.length += 1
        return True 

    def remove(self, index: int) -> Node:
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index=index)
        if not temp:
            return temp
        pre = self.get(index=index - 1)
        pre.next = temp.next
        temp.next = None
        return temp

    def reverse(self) -> None:
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next # !!!
            temp.next = before
            before = temp
            temp = after

        

if __name__ == "__main__":
    linked_list = LinkedList(randint(0,100))
    for i in range(6):
        linked_list.append(randint(0, 100))
    linked_list.show()
    linked_list.reverse()
    linked_list.show()

