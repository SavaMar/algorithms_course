class Node(object):
    def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None

class BinaryTree(object):
    def __init__(self, root):
      self.root = Node(root)

    def search(self, find_val):
      root = self.root

      """Return True if the value
      is in the tree, return
      False otherwise."""
      return self.preorder_search(root, find_val)

    def print_tree(self):
      """Print out all tree nodes
      as they are visited in
      a pre-order traversal."""
      root = self.root
      traversal = []
      traversal = self.preorder_print(root, traversal)
      print("travers: ", self.preorder_print(root, traversal))
      return ""

    def preorder_search(self, start, find_val):
      """Helper method - use this to create a 
      recursive search solution."""
      if start == None:
          return
      if start.value == find_val:
          return True
      
      if self.preorder_search(start.left, find_val):
          return True
      if self.preorder_search(start.right, find_val):
          return True
      return False

    def preorder_print(self, start, traversal):
      """Helper method - use this to create a 
      recursive print solution."""
      if start == None:
          return
      traversal.append(start.value)
      print(start.value)
      self.preorder_print(start.left, traversal)
      self.preorder_print(start.right, traversal)
      return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))

# Test print_tree
# Should be 1-2-4-5-3
print(tree.print_tree())