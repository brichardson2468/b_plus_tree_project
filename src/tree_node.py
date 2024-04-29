from b_plus_tree import max_keys

class TreeNode:
    def __init__(self, is_leaf=False):
        self.is_leaf = is_leaf   # Boolean to indicate if the node is a leaf node
        self.keys = []           # List to hold the keys
        self.children = []       # List to hold the references to child nodes
        self.next = None         # Reference to the next node (only applicable for leaf nodes)

    def insert(self, key, child=None):
        # Find the position where the new key should be inserted
        i = 0
        while i < len(self.keys) and self.keys[i] < key:
            i += 1
        
        # Insert the key at the found position
        self.keys.insert(i, key)
        
        # If this is not a leaf node, insert the child reference as well
        if not self.is_leaf:
            self.children.insert(i + 1, child)
        
        # Check if the node is full and needs to be split
        if self.is_full(max_keys):  # Assuming max_keys is defined or passed to the method
            return self.split()

    def split(self): # Helper method to split the node
        mid_index = len(self.keys) // 2
        mid_key = self.keys[mid_index]

        # Create a new node
        new_node = TreeNode(is_leaf=self.is_leaf)
        new_node.keys = self.keys[mid_index + 1:]
        self.keys = self.keys[:mid_index]
        
        if self.is_leaf:
            # If it's a leaf node, adjust the next pointers
            new_node.children = self.children[mid_index + 1:]
            self.children = self.children[:mid_index]
            new_node.next = self.next
            self.next = new_node
        else:
            # If it's not a leaf, move the child references
            new_node.children = self.children[mid_index + 1:]
            self.children = self.children[:mid_index + 1]
        
        return new_node, mid_key

    def is_full(self, max_keys): # Helper method to check if the node is full
        return len(self.keys) >= max_keys
