
class TreeNode:
    max_keys = 4
    
    def __init__(self, keys=None, children=None, is_leaf=False, parent=None):
        self.keys = keys if keys is not None else []
        self.records = {}  # Dictionary to hold lists of records for each key
        self.children = children if children is not None else []
        self.is_leaf = is_leaf
        self.next = None  # For leaf nodes, pointer to next leaf node
        self.parent = parent

    def insert(self, key, record=None, child=None):
        # Find the position where the new key should be inserted
        i = 0
        while i < len(self.keys) and self.keys[i] < key:
            i += 1
        
        if i < len(self.keys) and self.keys[i] == key:
            # Key already exists, append record
            self.records[key].append(record)
        
        else:
            # Insert new key and initialize record list
            self.keys.insert(i, key)
            self.records[key] = [record] if self.is_leaf else None
        
        if not self.is_leaf:
            self.children.insert(i + 1, child)
            if child:
                child.parent = self

        if self.is_full():
            return self.split()

    def split(self): # Helper method to split the node
        mid_index = len(self.keys) // 2
        mid_key = self.keys[mid_index]

        # Create a new node
        new_node = TreeNode(is_leaf=self.is_leaf, parent=self.parent)
        if self.is_leaf:
            # It's a leaf node, distribute keys and associated records
            new_node.keys = self.keys[mid_index:]
            new_node.records = {key: self.records.pop(key) for key in new_node.keys}
            new_node.next = self.next
            self.next = new_node
            self.keys = self.keys[:mid_index]
        else:
            # If it's not a leaf, move the child references
            new_node.keys = self.keys[mid_index + 1:]
            new_node.children = self.children[mid_index + 1:]
            self.keys = self.keys[:mid_index]
            self.children = self.children[:mid_index + 1]

            for child in new_node.children: # Update the parent reference of the child nodes
                child.parent = new_node
        return new_node, mid_key

    def is_full(self): # Helper method to check if the node is full
        return len(self.keys) >= self.max_keys
