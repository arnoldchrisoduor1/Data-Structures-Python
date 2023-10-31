#Deleting elements using the maximum elements from the left.

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data =  data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data == data:
            return 
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True
        
        if self.data < val:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if self.data > val:
            if self.right:
                return self.right.search(val)
            else:
                return False
            
    def in_order_transversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_transversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_transversal()

        return elements
    
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)

        if val > self.data:
            if self.right:
                self.right = self.right.delete(val)

        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
        max_val = self.left.find_max()
        self.data = max_val
        self.left = self.left.delete(max_val)

    
def build_tree(elements):
    print("Building a tree with the following elements: ", elements)
    
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root
    
if __name__ == '__main__':
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(20)
    print("After deleting 20 ",numbers_tree.in_order_transversal()) 

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(9)
    print("After deleting 9 ",numbers_tree.in_order_transversal())  

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(17)
    print("After deleting 17 ",numbers_tree.in_order_transversal()) 
