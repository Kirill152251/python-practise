class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()

def sort_stack(item: Stack) -> None:
    """
    Create a new instance of the Stack class called sorted_stack.
    While the input stack is not empty, perform the following:
    1. Pop the top element from the input stack and store it
    in a variable temp.
    2. While the sorted_stack is not empty and its top element is 
    greater than temp, pop the top element from sorted_stack and 
    push it back onto the input stack.
    3. Push the temp variable onto the sorted_stack.
    
    Once the input stack is empty, transfer the elements back 
    from sorted_stack to the input stack. To do this, 
    while sorted_stack is not empty, pop the top element 
    from sorted_stack and push it onto the input stack.
    """
    sorted_stack = Stack()
    while not item.is_empty():
        temp = item.pop()
        if sorted_stack.is_empty():
            sorted_stack.push(temp)
            continue
        while not sorted_stack.is_empty() and sorted_stack.peek() > temp: # This is the most important moment
            item.push(sorted_stack.pop())
        sorted_stack.push(temp)
    while not sorted_stack.is_empty():
        item.push(sorted_stack.pop())




my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()



"""
    EXPECTED OUTPUT:
    ----------------
    Stack before sort_stack():
    2
    4
    5
    1
    3

    Stack after sort_stack:
    1
    2
    3
    4
    5

"""