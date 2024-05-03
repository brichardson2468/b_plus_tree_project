from tree_node import TreeNode
import pandas as pd


class BPlusTree:
    def __init__(self, max_keys=4): # Initialize the B+ tree with a maximum number of keys
        self.root = TreeNode(is_leaf=True)
        self.max_keys = max_keys  # Maximum keys a node can hold
        self.min_keys = max_keys // 2 # Minimum keys a node can hold

    def insert(self, key, row): # Insert a key and its associated record into the B+ tree
        # Step 1: Find the leaf node where the key should be inserted
        print(f"Inserting key {key} with row data")
        leaf = self._find_leaf(key)

        # Step 2: Check if the key already exists in the leaf node
        if key in leaf.records:
            # If the key exists, check if the associated record is a list
            if isinstance(leaf.records[key], list):
                # If it's a list, append the new record to the list
                leaf.records[key].append(row)
            else:
                # If it's not a list, create a new list with the existing record and the new record
                leaf.records[key] = [leaf.records[key], row]
        # If the key does not exist, insert the key and the record into the leaf node
        else:
            leaf.insert(key, row)

        # Step 3: Check if the node has overflowed and handle splits
        if leaf.is_full():
            self._handle_split(leaf)
        
    def search_date_in_range(self, target_date):
        target_date = pd.to_datetime(target_date).date()
        print("Target date for search:", target_date)
        current_node = self.root

        # Traverse down to find the appropriate leaf node
        while not current_node.is_leaf:
            i = 0
            while i < len(current_node.keys) and target_date >= pd.Timestamp(current_node.keys[i]):
                #print("Current node key being compared:", current_node.keys[i])
                i += 1
            current_node = current_node.children[i]
            #print("Moved to child node:", i)

        # Now traverse the leaf nodes to find the target date
        results = []
        while current_node:
            # Assuming the first key in a node gives the minimum date
            if current_node.keys and (current_node.keys[0]) > target_date:
                print("Stopping search, keys in node are past the target date.")
                break

            for key in current_node.keys:
                #print("Leaf node key:", key)  # Check keys in the leaf node
                if key in current_node.records:
                    for record in current_node.records[key]:
                        start_date = pd.to_datetime(record['Time Period Start Date']).date()
                        end_date = pd.to_datetime(record['Time Period End Date']).date()
                        #print("Start Date:", start_date, "End Date:", end_date)
                        if start_date <= target_date <= end_date:
                            results.append(record)
            current_node = current_node.next

        print("Collected results:", results)
        return results

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
        print(f"Handling split for node with keys: {node.keys}")
        new_node, mid_key = node.split()
        if node == self.root:
            # Special case: split the root
            self._split_root()
        else:
            parent = node.parent
            parent.insert(mid_key, new_node)
            if parent.is_full(self.max_keys):
                self._handle_split(parent)

