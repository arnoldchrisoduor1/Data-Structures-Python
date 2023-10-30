class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_management_tree():
    #CTO hierarchy
    infra_head = TreeNode("Vishwa", "Infrastructure Head")
    infra_head.add.child(TreeNode("Dhaval", "Cloud Manager"))
    infra_head.add.child(TreeNode("Abhijit", "Cloud Manager"))

if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name")
    root_node.print_tree("designation")
    root_node.print_tree("both")