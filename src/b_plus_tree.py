from tree_node import TreeNode

class BPlusTree:
    def __init__(self, max_keys=4):
        self.root = TreeNode(is_leaf=True)
        self.max_keys = max_keys  # Maximum keys a node can hold

    def insert(self, key, record):
        """Insert a key along with its record into the B+ tree."""
        pass

    def search(self, key):
        """Search for a key in the B+ tree and return its associated record."""
        pass

    def delete(self, key):
        """Delete a key from the B+ tree."""
        pass

    def search_range(self, start_key, end_key):
        """Search for all records within a specified range."""
        pass

    def _split_root(self):
        """Split the root if necessary."""
        pass

    def _find_leaf(self, key):
        """Helper method to find the leaf node that should contain the key."""
        pass