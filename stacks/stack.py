class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
        
    def size(self):
        return len(self.items)
    
if __name__ == '__main__':
    my_stack = Stack()

    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)

    print("Peek:", my_stack.peek())
    print("Size:", my_stack.size())

    item = my_stack.pop()
    print("Popped item:", item)

    print("Is empty?", my_stack.is_empty())