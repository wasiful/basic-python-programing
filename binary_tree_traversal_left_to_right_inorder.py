class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        else:
            print("Traversal type" + str(traversal_type) + "is not supported.")
            return False

    def preorder_print(self, start, traversal):
        """root-> left-> right"""
        if start:
            traversal += (str(start.value)+ "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """Left -> root -> right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

                #          1
                #     2           3
                # 4       5   6       7
tree = BinaryTree(1)
tree.root.left = Node(2)  # creating left child of root node and setting the value 2
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print(tree.print_tree("preorder"))  # shows the left most child first and then goes for right, order up to down

print(tree.print_tree("inorder"))   # order down to top root node, takes left most child first

