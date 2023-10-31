#Deleting nodes using the min element from the left subtree.

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
    
    def post_order_transversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_transversal()
        if self.right:
            elements += self.right.post_order_transversal()
        elements.append(self.data)
        return elements
    
    def pre_order_transversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_transversal()
        if self.right:
            elements += self.right.pre_order_transversal()
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
    
    def calculate_sum(self):
        total_sum = self.data
        if self.left:
            total_sum += self.left.calculate_sum()
        if self.right:
            total_sum += self.right.calculate_sum()
        return total_sum
    
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("Before deleting the tree: ",numbers_tree.in_order_transversal())
    numbers_tree.delete(17)
    print("After deleting 17: ",numbers_tree.in_order_transversal())