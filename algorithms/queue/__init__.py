class Node:

    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None
        
class Queue:

    def __init__(self, value) -> None:
        node = Node(value=value)
        self.first = node
        self.last = node
        self.length = 1

    def enqueue(self, value) -> None:
        """Add item to the END of queue"""
        node = Node(value=value)
        if self.length == 0:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.length += 1
        

my_queue = Queue(4)

print('First:', my_queue.first.value)
print('Last:', my_queue.last.value)
print('Length:', my_queue.length)


"""
    EXPECTED OUTPUT:
    ----------------
    First: 4
    Last: 4
    Length: 1

"""