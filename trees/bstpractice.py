class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        pass

    def search(self, find_val):
        return False

    def print_tree(self):
        # [:-1] allows to omit the last element because we start at it before searching
        return self.preorder_print(tree.root, "")[:-1]

    def preorder_print(self, start, traversal):
        if start:
            # Append the starting value to the traversal variable
            traversal += (str(start.value) + '-')
            # print the value of nodes on the left side of the bfs queue
            traversal = self.preorder_print(start.left, traversal)
            # print the value of nodes at right side of bfs queue
            traversal = self.preorder_print(start.right, traversal)
        
        return traversal


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))
