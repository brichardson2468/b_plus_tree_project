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

    def _split_root(self): # Helper method to split the root node
        old_root = self.root
        # Split the old root
        new_right_node, mid_key = old_root.split()

        # Create a new root node which is not a leaf
        new_root = TreeNode(is_leaf=False)
        new_root.keys = [mid_key]
        new_root.children = [old_root, new_right_node]  # old_root is now the new_left_node

        # Set the new root as the tree's root
        self.root = new_root

    def _find_leaf(self, key): # Helper method to find the leaf node where the key should be inserted
        current_node = self.root
        while not current_node.is_leaf:  # Continue until a leaf node is reached
            # Traverse through the keys in the node to find appropriate child
            i = 0
            while i < len(current_node.keys) and key >= current_node.keys[i]:
                i += 1
            # Move to the next child node
            current_node = current_node.children[i]
        return current_node