class TreeNode:
    def __init__(self, is_leaf=False):
        self.is_leaf = is_leaf   # Boolean to indicate if the node is a leaf node
        self.keys = []           # List to hold the keys
        self.children = []       # List to hold the references to child nodes

    def insert(self, key, child=None):
        """Insert a key into the node. If it is an internal node, insert the child reference."""
        # This method will need to handle splitting the node if it gets too full
        pass

    def split(self):
        """Split the node into two and return the new node and the middle key."""
        pass

    def is_full(self, max_keys):
        """Determine if the node needs to be split."""
        return len(self.keys) >= max_keys
