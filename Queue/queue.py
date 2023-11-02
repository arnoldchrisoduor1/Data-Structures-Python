class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None
        
    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None
        
    def size(self):
        return len(self.items)
    
if __name__ == '__main__':
    my_queue = Queue()

    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)

    print("Front:", my_queue.front())
    print("Size:", my_queue.size())

    item = my_queue.dequeue()
    print("Dequeued item:", item)

    print("Is empty?", my_queue.is_empty())