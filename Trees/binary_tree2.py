class BinarySearchTreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
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
        
    def in_order_transversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_transversal()

        #visiting the base node.
        elements.append(self.data)

        #visiting the right node.
        if self.right:
            elements += self.right.in_order_transversal()

        return elements
    
    def search(self,val):
        if self.data == val:
            return True
        
        #checkig for the val in the left sub-tree.
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
            
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
            
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.search(3))

min_element = numbers_tree.find_min()
print("Minimum element in the binary search tree:", min_element)

max_element = numbers_tree.find_max()
print("The maximum number in the tree is: ", max_element)

