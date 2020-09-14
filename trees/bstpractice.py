class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)
    
    # helper will check for conditions such as being less than new_val
    # and looking to the current node's left and right of the tree
    def insert_helper(self, current_node, new_val):
        if current_node.value < new_val: # if the current node's value is less then the new value
            if current_node.right: # if there are children on the right branch of the node
                self.insert_helper(current_node.right, new_val) # insert a new node child on current_node
            else:
                current_node.right = Node(new_val) # initalize a new Node to populate
        else:
            if current_node.left:
                self.insert_helper(current_node.left, new_val) # insert the node if it is a new value
            else:
                current_node.left = Node(new_val) # initalize a new Node object that has a larger value

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, current_node, find_val)
        if current_node:
            if current_node.value == find_val:
                return True
            elif current_node.value < find_val:
                return self.search_helper(current_node.right, find_val)
            else
                return self.search_helper(current_node.left, find_val)
        
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
