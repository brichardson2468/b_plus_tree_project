from tree_node import TreeNode

class BPlusTree:
    def __init__(self, max_keys=4): # Initialize the B+ tree with a maximum number of keys
        self.root = TreeNode(is_leaf=True)
        self.max_keys = max_keys  # Maximum keys a node can hold
        self.min_keys = max_keys // 2 # Minimum keys a node can hold

    def insert(self, key, record): # Insert a key and its associated record into the B+ tree
        # Step 1: Find the leaf node where the key should be inserted
        leaf = self._find_leaf(key)

        # Step 2: Insert the key and the record into the leaf node
        # Assuming the record is just a value that can be stored directly in keys for simplicity
        leaf.insert(key, record)

        # Step 3: Check if the node has overflowed and handle splits
        if leaf.is_full(self.max_keys):
            self._handle_split(leaf)

    def search(self, key): # Search for a key in the B+ tree and return its associated record
        current_node = self.root
        while not current_node.is_leaf:
            i = 0
            while i < len(current_node.keys) and key >= current_node.keys[i]:
                i += 1
            current_node = current_node.children[i]
        # At the leaf node, look for the key
        if key in current_node.keys:
            return current_node.records[current_node.keys.index(key)]
        else:
            return None

    def delete(self, key):
        # Step 1: Find the leaf node where the key should be deleted
        leaf = self._find_leaf(key)
        if key not in leaf.keys:
            return False  # Key not found
        
        # Step 2: Remove the key
        index = leaf.keys.index(key)
        leaf.keys.pop(index)
        leaf.records.pop(index)  # Assuming records are stored in a list parallel to keys

        # Step 3: Handle underflow
        if len(leaf.keys) < self.min_keys:  # Assuming min_keys is defined
            self._handle_underflow(leaf)

        return True

    def search_range(self, start_key, end_key): 
        # Search for keys within a given range and return their associated records
        current_node = self.root
        results = []
        # Traverse to the leaf node for the start_key
        while not current_node.is_leaf:
            i = 0
            while i < len(current_node.keys) and start_key >= current_node.keys[i]:
                i += 1
            current_node = current_node.children[i]
        # Collect all records from start_key to end_key
        while current_node:
            for key, record in zip(current_node.keys, current_node.records):
                if start_key <= key <= end_key:
                    results.append(record)
            current_node = current_node.next
        return results

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
    
    def _handle_split(self, node): # Helper method to handle node splits
        # Recursively handle the splitting of nodes up to the root
        new_node, mid_key = node.split()
        if node == self.root:
            # Special case: split the root
            self._split_root()
        else:
            parent = node.parent
            parent.insert(mid_key, new_node)
            if parent.is_full(self.max_keys):
                self._handle_split(parent)

    def _handle_underflow(self, node):
        parent = node.parent
        left_sibling = None
        right_sibling = None
        index = 0

        # Find node's position in parent's children list and identify siblings
        if parent:
            index = parent.children.index(node)
            if index > 0:
                left_sibling = parent.children[index - 1]
            if index < len(parent.children) - 1:
                right_sibling = parent.children[index + 1]

        # Try to borrow from the left sibling
        if left_sibling and len(left_sibling.keys) > self.min_keys:
            self._borrow_from_left(node, left_sibling, parent, index)
            return

        # Try to borrow from the right sibling
        if right_sibling and len(right_sibling.keys) > self.min_keys:
            self._borrow_from_right(node, right_sibling, parent, index)
            return

        # If borrowing is not possible, merge with a sibling
        if left_sibling:
            self._merge_nodes(left_sibling, node, parent, index - 1)
        elif right_sibling:
            self._merge_nodes(node, right_sibling, parent, index)

    def _borrow_from_left(self, node, left_sibling, parent, index):
        # Borrow the last key from the left sibling
        borrow_key = left_sibling.keys.pop(-1)
        borrow_record = left_sibling.records.pop(-1)
        node.keys.insert(0, borrow_key)
        node.records.insert(0, borrow_record)

        # Update parent key
        parent.keys[index - 1] = node.keys[0]

    def _borrow_from_right(self, node, right_sibling, parent, index):
        # Borrow the first key from the right sibling
        borrow_key = right_sibling.keys.pop(0)
        borrow_record = right_sibling.records.pop(0)
        node.keys.append(borrow_key)
        node.records.append(borrow_record)

        # Update parent key
        parent.keys[index] = right_sibling.keys[0]

    def _merge_nodes(self, left, right, parent, parent_index):
        # Merge right node into left node
        left.keys.extend(right.keys)
        left.records.extend(right.records)
        if left.is_leaf:
            left.next = right.next
        else:
            left.children.extend(right.children)

        # Remove the right node and the parent key
        parent.keys.pop(parent_index)
        parent.children.pop(parent_index + 1)

        # If parent is underfull, handle underflow
        if len(parent.keys) < self.min_keys:
            self._handle_underflow(parent)