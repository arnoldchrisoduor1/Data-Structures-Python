#Creating a doubly linked list.

#creating a node class representing the elements.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

#Creating the doubly linked list plus functions.

#Creating the head.
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
    
    def delete(self, value):
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                return
            current = current.next

    def transverse(self):
        current = self.head
        while current:
            print(current.value, end="<->")
            current = current.next
        print("None")

    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
    
    def reverse(self):
        current = self.head
        while current:
            current.prev, current.next = current.next, current.prev
            if not current.next:
                self.head = current
            current = current.prev

#Using the doubly linked list.

my_doubly_linked_list = DoublyLinkedList()

my_doubly_linked_list.append(10)
my_doubly_linked_list.append(20)
my_doubly_linked_list.append(30)
my_doubly_linked_list.append(40)
my_doubly_linked_list.append(50)

my_doubly_linked_list.delete(20)

my_doubly_linked_list.transverse()

print(my_doubly_linked_list.search(10))
print(my_doubly_linked_list.search(20))

my_doubly_linked_list.reverse()

my_doubly_linked_list.transverse()

my_doubly_linked_list.transverse()
